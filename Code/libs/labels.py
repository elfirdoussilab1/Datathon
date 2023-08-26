import numpy as np

gics_sector = {
    'Energy' : 1,
    'Materials' : 2,
    'Industrials' : 3,
    'Consumer Discretionary' : 4,
    'Consumer Staples': 5,
    'Health Care' : 6,
    'Financials' : 7,
    'Information Technology' : 8,
    'Communication Services' : 9,
    'Utilities' : 10,
    'Real Estate' : 11
}



gics_industry_groups = {
    "Automobiles and Components": 251020,
    "Banks": 401010,
    "Capital Goods": 201030,
    "Commercial & Professional Services": 208030,
    "Consumer Durables & Apparel": 252010,
    "Consumer Services": 253010,
    "Diversified Financials": 401020,
    "Energy": 101010,
    "Food, Beverage, & Tobacco": 302010,
    "Food and Staples Retailing": 301020,
    "Health Care Equipment and Services": 351020,
    "Household and Personal Products": 304010,
    "Insurance": 403010,
    "Materials": 151010,
    "Media and Entertainment": 259010,
    "Pharmaceuticals, Biotechnology, and Life Sciences": 354010,
    "Real Estate": 404010,
    "Retailing": 255040,
    "Semiconductors and Semiconductor Equipment": 453010,
    "Software and Services": 454010,
    "Technology Hardware and Equipment": 455010,
    "Telecommunication Services": 501010,
    "Transportation": 203040,
    "Utilities": 551010
}

company_type = {'Public Investment Firm': 0, 'Public Company': 1, 'Private Company': 2,
                   'Private Investment Firm': 3, 'Government Institution' : 4, 'Public Fund':5,
                   'Financial Service Investment Arm' : 6, 'Foundation/Charitable Institution':7,
                   'Educational Institution': 8}
geo_region = {
    'Asia / Pacific': 1,
    'United States and Canada': 2,
    'Europe': 3,
    'Latin America and Caribbean': 4,
    'Africa / Middle East': 5
}

sector_map = {
    'BRITISH AIRWAYS PLC' : {'GICSSector' : 'Industrials', 'GICSSubIndustry' : 'Airlines'},
    'CDC GROUP BV' : {'GICSSector' : 'Financials', 'GICSSubIndustry' : 'Diversified Banks'},
    'BAZALGETTE HOLDINGS LIMITED' : {'GICSSector' : 'Industrials', 'GICSSubIndustry' : 'Construction & Engineering'},
    'MACQUARIE BANK LIMITED' : {'GICSSector' : 'Financials', 'GICSSubIndustry' : 'Diversified Banks'},
    'CHINA CONSTRUCTION BANK CORPORATION LONDON BRANCH' : {'GICSSector' : 'Real Estate', 'GICSSubIndustry' : 'Retail REITs'},
    'IF PC INSURANCE LIMITED' : {'GICSSector' : 'Financials', 'GICSSubIndustry' : 'Property & Casualty Insurance'},
    'SCANIA SERVICES SA' : {'GICSSector' : 'Industrials', 'GICSSubIndustry' : 'Construction Machinery & Heavy Trucks'},
    'BANK OF CYPRUS HOLDINGS PUBLIC LIMITED COMPANY' : {'GICSSector' : 'Financials', 'GICSSubIndustry' : 'Diversified Banks'},
    'CITY OF ALBANY' : {'GICSSector' : 'Consumer Discretionary', 'GICSSubIndustry' : 'Hotels, Resorts & Cruise Lines'},
    'DAVIS ZIFF PUBLISHING INC' : {'GICSSector' : 'Communication Services', 'GICSSubIndustry' : 'Interactive Media & Services'},
    'KG MYANMAR' : {'GICSSector' : 'Real Estate', 'GICSSubIndustry' : 'Diversified REITs'},
    'FORT WORTH TEXAS' : {'GICSSector' : 'Consumer Discretionary', 'GICSSubIndustry' : 'Specialized Consumer Services'},
    'BSB' : {'GICSSector' : 'Financials', 'GICSSubIndustry' : 'Diversified Banks'},
    'NVENT MANAGEMENT COMPANY' : {'GICSSector' : 'Industrials', 'GICSSubIndustry' : 'Electrical Components & Equipment'},
    'EATON CAPITAL' : {'GICSSector' : 'Industrials', 'GICSSubIndustry' : 'Electrical Components & Equipment'},
    'ZF SERVICES UK LIMITED' : {'GICSSector' : 'Consumer Discretionary', 'GICSSubIndustry' : 'Auto Parts & Equipment'},
    'BHUTAN' : {'GICSSector' : 'Consumer Staples', 'GICSSubIndustry' : 'Agricultural Products'},
    'MALLINCKRODT AG' : {'GICSSector' : 'Health Care', 'GICSSubIndustry' : 'Pharmaceuticals'}
}

sub_industry_map = {'Computer Hardware' : 'Electrical Components & Equipment' ,
 'Computer Storage & Peripherals' : 'Electrical Components & Equipment',
 'Diversified Commercial & Professional Services' : 'Human Resource & Employment Services',
 'Real Estate Investment Trusts' : 'Diversified REITs' }

SICCODE_map = {'Computer Hardware' : 'Electrical Components & Equipment' ,
 'Computer Storage & Peripherals' : 'Electrical Components & Equipment',
 'Diversified Commercial & Professional Services' : 'Human Resource & Employment Services',
 'Real Estate Investment Trusts' : 'Diversified REITs' }

country_code_map = {
	"Andorra": "AD",
    "United Arab Emirates": "AE",
    "Afghanistan": "AF",
    "Antigua and Barbuda": "AG",
    "Antigua & Barbuda": "AG",
    "Anguilla": "AI",
    "Albania": "AL",
    "Armenia": "AM",
    "Angola": "AO",
    "Antarctica": "AQ",
    "Argentina": "AR",
    "American Samoa": "AS",
    "Austria": "AT",
    "Australia": "AU",
    "Aruba": "AW",
    "Åland Islands": "AX",
    "Azerbaijan": "AZ",
    "Bosnia and Herzegovina": "BA",
    "Barbados": "BB",
    "Bangladesh": "BD",
    "Belgium": "BE",
    "Burkina Faso": "BF",
    "Bulgaria": "BG",
    "Bahrain": "BH",
    "Burundi": "BI",
    "Benin": "BJ",
    "Saint Barthélemy": "BL",
    "Bermuda": "BM",
    "Brunei Darussalam": "BN",
    "Bolivia": "BO",
    "Bolivia (Plurinational State of)": "BO",
    "Bonaire, Sint Eustatius and Saba": "BQ",
    "Bonaire, Sint Eustatius & Saba": "BQ",
    "Brazil": "BR",
    "Bahamas": "BS",
    "Bhutan": "BT",
    "Bouvet Island": "BV",
    "Botswana": "BW",
    "Belarus": "BY",
    "Belize": "BZ",
    "Canada": "CA",
    "Cocos Islands": "CC",
    "Cocos": "CC",
    "Cocos (Keeling) Islands": "CC",
    "Democratic Republic of the Congo": "CD",
    "Central African Republic": "CF",
    "Congo": "CG",
    "Switzerland": "CH",
    "Côte d'Ivoire": "CI",
    "Cook Islands": "CK",
    "Chile": "CL",
    "Cameroon": "CM",
    "China": "CN",
    "Colombia": "CO",
    "Costa Rica": "CR",
    "Cuba": "CU",
    "Cabo Verde": "CV",
    "Curaçao": "CW",
    "Christmas Island": "CX",
    "Cyprus": "CY",
    "Czechia": "CZ",
    "Czech Republic": "CZ",
    "Czech": "CZ",
    "Germany": "DE",
    "Djibouti": "DJ",
    "Denmark": "DK",
    "Dominica": "DM",
    "Dominican Republic": "DO",
    "Algeria": "DZ",
    "Ecuador": "EC",
    "Estonia": "EE",
    "Egypt": "EG",
    "Western Sahara": "EH",
    "Eritrea": "ER",
    "Spain": "ES",
    "Ethiopia": "ET",
    "Finland": "FI",
    "Fiji": "FJ",
    "Malvinas Falkland Islands": "FK",
    "Falkland Islands": "FK",
    "Falkland Islands (Malvinas)": "FK",
    "Micronesia": "FM",
    "Micronesia (Federated States of)": "FM",
    "Faroe Islands": "FO",
    "France": "FR",
    "Gabon": "GA",
    "United Kingdom of Great Britain and Northern Ireland": "GB",
    "United Kingdom of Great Britain & Northern Ireland" : "GB",
    "Grenada": "GD",
    "Georgia": "GE",
    "French Guiana": "GF",
    "Guernsey": "GG",
    "Ghana": "GH",
    "Gibraltar": "GI",
    "Greenland": "GL",
    "Gambia": "GM",
    "Guinea": "GN",
    "Guadeloupe": "GP",
    "Equatorial Guinea": "GQ",
    "Greece": "GR",
    "South Georgia and the South Sandwich Islands": "GS",
    "South Georgia & the South Sandwich Islands": "GS",
    "Guatemala": "GT",
    "Guam": "GU",
    "Guinea-Bissau": "GW",
    "Guyana": "GY",
    "Hong Kong": "HK",
    "Heard Island and McDonald Islands": "HM",
    "Heard Island & McDonald Islands": "HM",
    "Honduras": "HN",
    "Croatia": "HR",
    "Haiti": "HT",
    "Hungary": "HU",
    "Indonesia": "ID",
    "Ireland": "IE",
    "Israel": "IL",
    "Isle of Man": "IM",
    "India": "IN",
    "British Indian Ocean Territory": "IO",
    "Iraq": "IQ",
    "Iran": "IR",
    "Iran (Islamic Republic of)": "IR",
    "Islamic Republic of Iran": "IR",
    "Iceland": "IS",
    "Italy": "IT",
    "Jersey": "JE",
    "Jamaica": "JM",
    "Jordan": "JO",
    "Japan": "JP",
    "Kenya": "KE",
    "Kyrgyzstan": "KG",
    "Cambodia": "KH",
    "Kiribati": "KI",
    "Comoros": "KM",
    "Saint Kitts and Nevis": "KN",
    "Korea (Democratic People's Republic of)": "KP",
    "Democratic People's Republic of Korea": "KP",
    "North Korea": "KP",
    "Korea, Republic of": "KR",
    "Republic of Korea": "KR",
    "South Korea":"KR",
    "Kuwait": "KW",
    "Cayman Islands": "KY",
    "Kazakhstan": "KZ",
    "Lao People's Democratic Republic": "LA",
    "Lebanon": "LB",
    "Saint Lucia": "LC",
    "Liechtenstein": "LI",
    "Sri Lanka": "LK",
    "Liberia": "LR",
    "Lesotho": "LS",
    "Lithuania": "LT",
    "Luxembourg": "LU",
    "Latvia": "LV",
    "Libya": "LY",
    "Morocco": "MA",
    "Monaco": "MC",
    "Moldova, Republic of": "MD",
    "Montenegro": "ME",
    "Saint Martin (French part)": "MF",
    "Madagascar": "MG",
    "Marshall Islands": "MH",
    "North Macedonia": "MK",
    "Mali": "ML",
    "Myanmar": "MM",
    "Mongolia": "MN",
    "Macao": "MO",
    "Northern Mariana Islands": "MP",
    "Martinique": "MQ",
    "Mauritania": "MR",
    "Montserrat": "MS",
    "Malta": "MT",
    "Mauritius": "MU",
    "Maldives": "MV",
    "Malawi": "MW",
    "Mexico": "MX",
    "Malaysia": "MY",
    "Mozambique": "MZ",
    "Namibia": "NA",
    "New Caledonia": "NC",
    "Niger": "NE",
    "Norfolk Island": "NF",
    "Nigeria": "NG",
    "Nicaragua": "NI",
    "Netherlands": "NL",
    "Norway": "NO",
    "Nepal": "NP",
    "Nauru": "NR",
    "Niue": "NU",
    "New Zealand": "NZ",
    "Oman": "OM",
    "Panama": "PA",
    "Peru": "PE",
    "French Polynesia": "PF",
    "Papua New Guinea": "PG",
    "Philippines": "PH",
    "Pakistan": "PK",
    "Poland": "PL",
    "Saint Pierre and Miquelon": "PM",
    "Pitcairn": "PN",
    "Puerto Rico": "PR",
    "Palestine, State of": "PS",
    "Portugal": "PT",
    "Palau": "PW",
    "Paraguay": "PY",
    "Qatar": "QA",
    "Réunion": "RE",
    "Romania": "RO",
    "Serbia": "RS",
    "Russian Federation": "RU",
    "Russia": "RU",
    "Rwanda": "RW",
    "Saudi Arabia": "SA",
    "Solomon Islands": "SB",
    "Seychelles": "SC",
    "Sudan": "SD",
    "Sweden": "SE",
    "Singapore": "SG",
    "Saint Helena, Ascension and Tristan da Cunha": "SH",
    "Saint Helena, Ascension & Tristan da Cunha": "SH",
    "Slovenia": "SI",
    "Svalbard and Jan Mayen": "SJ",
    "Slovakia": "SK",
    "Sierra Leone": "SL",
    "San Marino": "SM",
    "Senegal": "SN",
    "Somalia": "SO",
    "Suriname": "SR",
    "South Sudan": "SS",
    "Sao Tome and Principe": "ST",
    "Sao Tome & Principe": "ST",
    "El Salvador": "SV",
    "Sint Maarten (Dutch part)": "SX",
    "Syrian Arab Republic": "SY",
    "Eswatini": "SZ",
    "Turks and Caicos Islands": "TC",
    "Chad": "TD",
    "French Southern Territories": "TF",
    "Togo": "TG",
    "Thailand": "TH",
    "Tajikistan": "TJ",
    "Tokelau": "TK",
    "Timor-Leste": "TL",
    "Turkmenistan": "TM",
    "Tunisia": "TN",
    "Tonga": "TO",
    "Turkey": "TR",
    "Trinidad and Tobago": "TT",
    "Trinidad & Tobago": "TT",
    "Tuvalu": "TV",
    "Taiwan, Province of China": "TW",
    "Taiwan": 'TW',
    "Tanzania, United Republic of": "TZ",
    "Tanzania": "TZ",
    "United Republic of of Tanzania": "TZ",
    "Ukraine": "UA",
    "Uganda": "UG",
    "United States Minor Outlying Islands": "UM",
    "United States of America": "US",
    "United States": "US",
    "USA": "US",
    "United Kingdom": "UK",
    "Uruguay": "UY",
    "Uzbekistan": "UZ",
    "Holy See": "VA",
    "Saint Vincent and the Grenadines": "VC",
    "Saint Vincent & the Grenadines": "VC",
    "Venezuela (Bolivarian Republic of)": "VE",
    "Venezuela": "VE",
    "Bolivarian Republic of Venezuela": "VE",
    "Virgin Islands (British)": "VG",
    "British Virgin Islands": "VG",
    "Virgin Islands (U.S.)": "VI",
    "U.S. Virgin Islands": "VI",
    "Virgin Islands": "VI",
    "Viet Nam": "VN",
    "Vietnam": "VN",
    "Vanuatu": "VU",
    "Wallis and Futuna": "WF",
    "Wallis & Futuna": "WF",
    "Samoa": "WS",
    "Yemen": "YE",
    "Mayotte": "YT",
    "South Africa": "ZA",
    "Zambia": "ZM",
    "Zimbabwe": "ZW",
    np.nan : "ZZ"
}

encode_country_map = country_code_map
count = 0
# initilizing with the first value of the 
v_prev = "AD"
for key, value in encode_country_map.items():
    
    if count > 0:
        # we compare previous value and this new one to see if we increment count
        if value != v_prev:
            count += 1
            encode_country_map[key] = count
            v_prev = value
        else:
            encode_country_map[key] = count
    else :
        encode_country_map[key] = count
        count += 1




