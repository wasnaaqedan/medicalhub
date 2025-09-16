#!/usr/bin/env python3
"""
PostgreSQL Database Setup Script for Medical Hub
This script creates the database and initializes the schema
"""

import os
import sys
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

def create_database():
    """Create the PostgreSQL database"""
    try:
        # Connect to PostgreSQL server (default database)
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            user="postgres",
            password="postgres",
            database="postgres"  # Connect to default database first
        )
        conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cursor = conn.cursor()
        
        # Check if database exists
        cursor.execute("SELECT 1 FROM pg_database WHERE datname = 'medical_hub_db'")
        exists = cursor.fetchone()
        
        if not exists:
            # Create database
            cursor.execute("CREATE DATABASE medical_hub_db")
            print("✅ Database 'medical_hub_db' created successfully")
        else:
            print("ℹ️  Database 'medical_hub_db' already exists")
        
        cursor.close()
        conn.close()
        
        return True
        
    except psycopg2.Error as e:
        print(f"❌ Error creating database: {e}")
        return False

def test_connection():
    """Test connection to the new database"""
    try:
        conn = psycopg2.connect(
            host="localhost",
            port="5432",
            user="postgres",
            password="postgres",
            database="medical_hub_db"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        print(f"✅ Connected to PostgreSQL: {version[0]}")
        
        cursor.close()
        conn.close()
        return True
        
    except psycopg2.Error as e:
        print(f"❌ Error connecting to database: {e}")
        return False

def main():
    """Main setup function"""
    print("🚀 Setting up PostgreSQL database for Medical Hub...")
    print("=" * 50)
    
    # Check if psycopg2 is installed
    try:
        import psycopg2
    except ImportError:
        print("❌ psycopg2 is not installed. Please install it first:")
        print("   pip install psycopg2-binary")
        return False
    
    # Create database
    if not create_database():
        return False
    
    # Test connection
    if not test_connection():
        return False
    
    print("=" * 50)
    print("✅ PostgreSQL setup completed successfully!")
    print("\nNext steps:")
    print("1. Run: python run.py")
    print("2. The application will automatically create tables")
    print("3. Access your app at: http://localhost:5000")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

