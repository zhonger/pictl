"""Regions for different S3-like storage"""

regions = {
    "S3": [
        "us-east-1",
        "us-east-2",
        "us-west-1",
        "us-west-2",
        "af-south-1",
        "ap-east-1",
        "ap-south-2",
        "ap-southeast-3",
        "ap-southeast-4",
        "ap-south-1",
        "ap-south-2",
        "ap-northeast-3",
        "ap-northeast-2",
        "ap-southeast-1",
        "ap-southeast-2",
        "ap-northeast-1",
        "ca-central-1",
        "cn-north-1",
        "cn-northwest-1",
        "eu-central-1",
        "eu-west-1",
        "eu-west-2",
        "eu-south-1",
        "eu-west-3",
        "eu-north-1",
        "eu-south-2",
        "eu-central-2",
        "sa-east-1",
        "me-south-1",
        "me-central-1",
        "us-gov-east-1",
        "us-gov-west-1",
    ],
    "R2": [
        "us-east-1",
    ],
    "COS(Tencent)": [
        "ap-beijing-1",
        "ap-beijing",
        "ap-nanjing",
        "ap-shanghai",
        "ap-guangzhou",
        "ap-chengdu",
        "ap-chongqing",
        "ap-shenzhen-fsi",
        "ap-shanghai-fsi",
        "ap-beijing-fsi",
        "ap-hongkong",
        "ap-singapore",
        "ap-mumbai",
        "ap-jakarta",
        "ap-seoul",
        "ap-bangkok",
        "ap-tokyo",
        "na-siliconvalley",
        "na-ashburn",
        "na-toronto",
        "sa-saopaulo",
        "eu-frankfurt",
    ],
    "Oracle": [
        "af-johannesburg-1",
        "ap-chuncheon-1",
        "ap-hyderabad-1",
        "ap-melbourne-1",
        "ap-mumbai-1",
        "ap-osaka-1",
        "ap-seoul-1",
        "ap-singapore-1",
        "ap-sydney-1",
        "ap-tokyo-1",
        "ca-montreal-1",
        "ca-toronto-1",
        "eu-amsterdam-1",
        "eu-frankfurt-1",
        "eu-jovanovac-1",
        "eu-madrid-1",
        "eu-marseille-1",
        "eu-milan-1",
        "eu-paris-1",
        "eu-stockholm-1",
        "eu-zurich-1",
        "il-jerusalem-1",
        "me-abudhabi-1",
        "me-dubai-1",
        "me-jeddah-1",
        "mx-queretaro-1",
        "sa-santiago-1",
        "sa-saopaulo-1",
        "sa-vinhedo-1",
        "uk-cardiff-1",
        "uk-london-1",
        "us-ashburn-1",
        "us-chicago-1",
        "us-phoenix-1",
        "us-sanjose-1",
    ],
    "OSS(Aliyun)": [
        "cn-hangzhou",
        "cn-shanghai",
        "cn-nanjing",
        "cn-fuzhou",
        "cn-qingdao",
        "cn-beijing",
        "cn-zhangjiakou",
        "cn-huhehaote",
        "cn-wulanchabu",
        "cn-shenzhen",
        "cn-heyuan",
        "cn-guangzhou",
        "cn-chengdu",
        "cn-hongkong",
        "us-west-1",
        "us-east-1",
        "ap-northeast-1",
        "ap-northeast-2",
        "ap-southeast-1",
        "ap-southeast-2",
        "ap-southeast-3",
        "ap-southeast-5",
        "ap-southeast-6",
        "ap-southeast-7",
        "ap-south-1",
        "eu-central-1",
        "eu-west-1",
        "me-east-1",
        "rg-china-mainland",
    ],
    "B2": [
        "us-west-001",
        "us-west-002",
        "eu-central-003",
        "us-west-004",
        "us-east-005",
    ],
    "OBS(Huawei)": [
        "cn-north-1",
        "cn-north-4",
        "cn-east-2",
        "cn-east-3",
        "cn-south-1",
        "ap-southeast-1",
        "ap-southeast-2",
        "ap-southeast-3",
        "af-south-1",
        "la-north-2",
        "na-mexico-1",
        "sa-brazil-1",
        "la-south-2",
        "tr-west-1",
    ],
    "Vultr": ["sgp1", "ams1", "blr1", "del1", "ewr1", "sjc1"],
    "DO": ["ams3", "fra1", "nyc3", "sfo2", "sgp1"],
    "Linode": ["us-southeast-1", "eu-central-1", "us-east-1", "ap-south-1"],
    "GCP": [
        "NORTHAMERICA-NORTHEAST1",
        "NORTHAMERICA-NORTHEAST2",
        "US-CENTRAL1",
        "US-EAST1",
        "US-EAST4",
        "US-EAST5",
        "US-SOUTH1",
        "US-WEST1",
        "US-WEST2",
        "US-WEST3",
        "US-WEST4",
        "SOUTHAMERICA-EAST1",
        "SOUTHAMERICA-WEST1",
        "EUROPE-CENTRAL2",
        "EUROPE-NORTH1",
        "EUROPE-SOUTHWEST1",
        "EUROPE-WEST1",
        "EUROPE-WEST2",
        "EUROPE-WEST3",
        "EUROPE-WEST4",
        "EUROPE-WEST6",
        "EUROPE-WEST8",
        "EUROPE-WEST9",
        "EUROPE-WEST12",
        "ASIA-EAST1",
        "ASIA-EAST2",
        "ASIA-NORTHEAST1",
        "ASIA-NORTHEAST2",
        "ASIA-NORTHEAST3",
        "ASIA-SOUTHEAST1",
        "ASIA-SOUTH1",
        "ASIA-SOUTH2",
        "ASIA-SOUTHEAST2",
        "ME-CENTRAL1",
        "ME-WEST1",
        "AUSTRALIA-SOUTHEAST1",
        "AUSTRALIA-SOUTHEAST2",
        "ASIA",
        "EU",
        "IN",
        "US",
    ],
    "Kodo(Qiniu)": [
        "cn-east-1",
        "cn-east-2",
        "cn-north-1",
        "cn-south-1",
        "us-north-1",
        "ap-southeast-1",
    ],
    "minio": ["us-east-1"],
    "US3": [
        "cn-bj",
        "cn-wlcb",
        "cn-sh2",
        "cn-gd",
        "hk",
        "us-ca",
        "sg",
        "idn-jakarta",
        "tw-tp",
        "afr-nigeria",
        "bra-saopaulo",
        "uae-dubai",
        "ge-fra",
        "vn-sng",
        "us-ws",
        "ind-mumbai",
        "kr-seoul",
        "jpn-tky",
        "th-bkk",
    ],
    "QingStor": ["pek3a", "sh1a", "pek3b", "gd2", "ap3"],
    "OSS(JD)": ["cn-north-1", "cn-east-1", "cn-east-2", "cn-south-1"],
    "BOS(Baidu)": ["bj", "gz", "su", "bd", "fwh", "fsh", "hkg"],
    "KS3(Kingsoft)": [
        "cn-beijing",
        "cn-shanghai",
        "cn-guangzhou",
        "cn-hk-1",
        "rus",
        "sgp",
        "jr-beijing",
        "jr-shanghai",
    ],
    "Scaleway": ["nl-ams", "fr-par", "pl-waw"],
}
