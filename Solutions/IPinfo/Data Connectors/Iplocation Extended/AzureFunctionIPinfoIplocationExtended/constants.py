import os

__all__ = [
    'RESOURCE_ID', 'IPINFO_TOKEN', 'TENANT_ID', 'CLIENT_ID', 'CLIENT_SECRET',
    'LOCATION', 'SUBCRIPTION_ID', 'RESOURCE_GROUP_NAME',
    'WORKSPACE_NAME', 'RETENTION_IN_DAYS', 'TOTAL_RETENTION_IN_DAYS',
    'DATA_COLLECTION_ENDPOINT_NAME', 'LOCATION_EXTENDED_DCR_NAME', 'LOCATION_EXTENDED_TABLE_NAME',
    'LOCATION_EXTENDED_STREAM_DECLARATION', 'AZURE_SCOPE', 'AZURE_BASE_URL', 'IPINFO_BASE_URL',
    'MMDB_NAME', 'LOCATION_EXTENDED_TABLE_SCHEMA', 'LOCATION_EXTENDED_TABLE_COLUMNS'
]

# Enviornment Virables
RESOURCE_ID = os.environ["RESOURCE_ID"]
IPINFO_TOKEN = os.environ["IPINFO_TOKEN"]
TENANT_ID = os.environ["TENANT_ID"]
CLIENT_ID = os.environ["CLIENT_ID"]
CLIENT_SECRET = os.environ["CLIENT_SECRET"]
RETENTION_IN_DAYS = os.environ["RETENTION_IN_DAYS"]
TOTAL_RETENTION_IN_DAYS = os.environ["TOTAL_RETENTION_IN_DAYS"]
LOCATION = os.environ["LOCATION"]

parts = RESOURCE_ID.split("/")
SUBCRIPTION_ID = parts[2]
RESOURCE_GROUP_NAME = parts[4]
WORKSPACE_NAME = parts[8]

DATA_COLLECTION_ENDPOINT_NAME = "ipinfo-logs-ingestion"
LOCATION_EXTENDED_DCR_NAME = "ipinfo_rule_for_location_extended_table"
LOCATION_EXTENDED_TABLE_NAME = "Ipinfo_Location_extended_CL"
LOCATION_EXTENDED_STREAM_DECLARATION = "Custom-Ipinfo_Location_extended_CL"

AZURE_SCOPE = "https://management.azure.com/.default"
AZURE_BASE_URL = f"https://management.azure.com/subscriptions/{SUBCRIPTION_ID}/resourceGroups/{RESOURCE_GROUP_NAME}/providers/Microsoft."
IPINFO_BASE_URL = "https://ipinfo.io/data"
MMDB_NAME = "location_extended_v2.mmdb"

LOCATION_EXTENDED_TABLE_SCHEMA = {
    "properties": {
        "totalRetentionInDays": TOTAL_RETENTION_IN_DAYS,
        "archiveRetentionInDays": 0,
        "plan": "Analytics",
        "retentionInDaysAsDefault": True,
        "totalRetentionInDaysAsDefault": True,
        "schema": {
            "tableSubType": "DataCollectionRuleBased",
            "name": LOCATION_EXTENDED_TABLE_NAME,
            "tableType": "CustomLog",
            "description": "Range based table",
            "columns": [
                {"name": "city", "type": "string", "isDefaultDisplay": False, "isHidden": False},
                {"name": "country", "type": "string", "isDefaultDisplay": False, "isHidden": False},
				{"name": "country_name", "type": "string", "isDefaultDisplay": False, "isHidden": False},
                {"name": "latitude", "type": "string", "isDefaultDisplay": False, "isHidden": False},
                {"name": "longitude", "type": "string", "isDefaultDisplay": False, "isHidden": False},
                {"name": "postal_code", "type": "string", "isDefaultDisplay": False, "isHidden": False},
                {"name": "radius", "type": "string", "isDefaultDisplay": False, "isHidden": False},
                {"name": "region_name", "type": "string", "isDefaultDisplay": False, "isHidden": False},
				{"name": "region", "type": "string", "isDefaultDisplay": False, "isHidden": False},
                {"name": "timezone", "type": "string", "isDefaultDisplay": False, "isHidden": False},
				{"name": "geoname_id", "type": "string", "isDefaultDisplay": False, "isHidden": False},
				{"name": "ip_range", "type": "string", "isDefaultDisplay": False, "isHidden": False},
                {"name": "TimeGenerated", "type": "datetime", "isDefaultDisplay": False, "isHidden": False},
            ],
            "standardColumns": [{"name": "TenantId", "type": "guid", "isDefaultDisplay": False, "isHidden": False}],
            "solutions": ["LogManagement"],
            "isTroubleshootingAllowed": True,
        },
        "provisioningState": "Succeeded",
        "retentionInDays": RETENTION_IN_DAYS,
    },
    "id": f"/subscriptions/{SUBCRIPTION_ID}/resourceGroups/{RESOURCE_GROUP_NAME}/providers/Microsoft.OperationalInsights/workspaces/{WORKSPACE_NAME}/tables/{LOCATION_EXTENDED_TABLE_NAME}",
    "name": LOCATION_EXTENDED_TABLE_NAME,
}

LOCATION_EXTENDED_TABLE_COLUMNS = {
    "columns": [
        {"name": "TimeGenerated", "type": "datetime"},
        {"name": "city", "type": "string"},
        {"name": "country", "type": "string"},
		{"name": "country_name", "type": "string"},
        {"name": "latitude", "type": "string"},
        {"name": "longitude", "type": "string"},
        {"name": "postal_code", "type": "string"},
		{"name": "radius", "type": "string"},
        {"name": "region_name", "type": "string"},
        {"name": "region", "type": "string"},
        {"name": "timezone", "type": "string"},
        {"name": "geoname_id", "type": "string"},
        {"name": "range", "type": "string"},
    ]
}
