/**
 * PostgreSQL Database Adapter for Sevenseas Broadband Lead Storage
 * Supports connection pooling via pg.Pool and provides resilient fallback.
 */

import { Pool } from "pg";
import fs from "fs";
import path from "path";

// Initialize PostgreSQL Pool if DATABASE_URL is provided
const connectionString = process.env.DATABASE_URL;

let pool: Pool | null = null;
if (connectionString) {
  pool = new Pool({
    connectionString,
    ssl: process.env.NODE_ENV === "production" ? { rejectUnauthorized: false } : undefined,
    max: 10,
    idleTimeoutMillis: 30000,
    connectionTimeoutMillis: 5000
  });

  // Automatically ensure table schema exists
  pool.query(`
    CREATE TABLE IF NOT EXISTS leads (
      id VARCHAR(64) PRIMARY KEY,
      created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
      full_name VARCHAR(120) NOT NULL,
      mobile_number VARCHAR(15) NOT NULL,
      area_locality VARCHAR(120) NOT NULL,
      society_building VARCHAR(120),
      preferred_plan VARCHAR(80) NOT NULL,
      ip_address VARCHAR(45),
      status VARCHAR(20) DEFAULT 'NEW'
    );
  `).catch(err => {
    console.warn("PostgreSQL table init note:", err.message);
  });
}

export interface LeadRecord {
  id: string;
  fullName: string;
  mobileNumber: string;
  areaLocality: string;
  societyBuilding?: string;
  preferredPlan: string;
  ipAddress?: string;
}

export async function insertLead(lead: LeadRecord): Promise<string> {
  const leadId = lead.id || `SSB-${Date.now()}-${Math.floor(Math.random() * 900 + 100)}`;

  if (pool) {
    try {
      await pool.query(
        `INSERT INTO leads (id, full_name, mobile_number, area_locality, society_building, preferred_plan, ip_address, status)
         VALUES ($1, $2, $3, $4, $5, $6, $7, $8)`,
        [
          leadId,
          lead.fullName,
          lead.mobileNumber,
          lead.areaLocality,
          lead.societyBuilding || "",
          lead.preferredPlan,
          lead.ipAddress || "127.0.0.1",
          "NEW"
        ]
      );
      return leadId;
    } catch (dbErr) {
      console.error("PostgreSQL insert failed, saving to local audit fallback:", dbErr);
    }
  }

  // File-based structured fallback (JSON audit trail)
  try {
    const backupDir = path.join(process.cwd(), "data");
    if (!fs.existsSync(backupDir)) {
      fs.mkdirSync(backupDir, { recursive: true });
    }
    const backupPath = path.join(backupDir, "leads.json");
    let leads: any[] = [];
    if (fs.existsSync(backupPath)) {
      leads = JSON.parse(fs.readFileSync(backupPath, "utf-8"));
    }
    leads.push({
      id: leadId,
      timestamp: new Date().toISOString(),
      ...lead,
      status: "NEW"
    });
    fs.writeFileSync(backupPath, JSON.stringify(leads, null, 2), "utf-8");
  } catch (fsErr) {
    console.error("File audit fallback error:", fsErr);
  }

  return leadId;
}
