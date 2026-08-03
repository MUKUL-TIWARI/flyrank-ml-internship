# Data Quality Report

## dim_clients

- Rows: **104**
- Columns: **9**
- Memory: **0.01 MB**
- Duplicate Rows: **0**

### Missing Values

| Column | Missing | % |
|--------|---------|---|
| client_hash_id | 0 | 0.0 |
| is_active | 10 | 9.62 |
| has_gsc_access | 10 | 9.62 |
| has_ga4_access | 10 | 9.62 |
| access_profile | 0 | 0.0 |
| client_created_date | 10 | 9.62 |
| client_updated_date | 10 | 9.62 |
| gsc_data_start | 37 | 35.58 |
| ga4_data_start | 53 | 50.96 |

---

## dim_content

- Rows: **519606**
- Columns: **26**
- Memory: **163.39 MB**
- Duplicate Rows: **0**

### Missing Values

| Column | Missing | % |
|--------|---------|---|
| client_hash_id | 0 | 0.0 |
| content_hash_id | 0 | 0.0 |
| keyword_hash_id | 71998 | 13.86 |
| url_hash_id | 6525 | 1.26 |
| keyword_char_count | 0 | 0.0 |
| keyword_token_count | 0 | 0.0 |
| url_char_count | 0 | 0.0 |
| content_created_date | 0 | 0.0 |
| content_updated_date | 0 | 0.0 |
| content_type | 0 | 0.0 |
| search_volume | 142622 | 27.45 |
| competition | 142622 | 27.45 |
| competition_level | 144456 | 27.8 |
| cpc | 142622 | 27.45 |
| main_intent | 148398 | 28.56 |
| backlinks | 267474 | 51.48 |
| category_count | 0 | 0.0 |
| keyword_created_date | 71998 | 13.86 |
| provider_used | 369936 | 71.2 |
| model_used | 84963 | 16.35 |
| char_count | 177768 | 34.21 |
| word_count | 177768 | 34.21 |
| last_optimized_date | 474210 | 91.26 |
| optimization_eligible_date | 474210 | 91.26 |
| is_published | 0 | 0.0 |
| is_deleted | 0 | 0.0 |

---

## fact_content_daily_performance

- Rows: **100000**
- Columns: **31**
- Memory: **28.04 MB**
- Duplicate Rows: **2**

### Missing Values

| Column | Missing | % |
|--------|---------|---|
| report_date | 0 | 0.0 |
| client_hash_id | 0 | 0.0 |
| content_hash_id | 0 | 0.0 |
| client_has_gsc | 0 | 0.0 |
| client_has_ga4 | 0 | 0.0 |
| gsc_data_available | 0 | 0.0 |
| ga4_data_available | 20616 | 20.62 |
| gsc_impressions | 0 | 0.0 |
| gsc_clicks | 0 | 0.0 |
| gsc_sum_position | 0 | 0.0 |
| gsc_avg_position | 66814 | 66.81 |
| ga4_pageviews | 20616 | 20.62 |
| ga4_sessions | 20616 | 20.62 |
| ga4_users | 20616 | 20.62 |
| ga4_engaged_sessions | 20616 | 20.62 |
| ga4_total_engagement_sec | 20616 | 20.62 |
| sessions_organic | 20616 | 20.62 |
| sessions_direct | 20616 | 20.62 |
| sessions_referral | 20616 | 20.62 |
| sessions_social | 20616 | 20.62 |
| sessions_paid | 20616 | 20.62 |
| sessions_ai | 20616 | 20.62 |
| ai_chatgpt | 20616 | 20.62 |
| ai_perplexity | 20616 | 20.62 |
| ai_gemini | 20616 | 20.62 |
| ai_copilot | 20616 | 20.62 |
| ai_claude | 20616 | 20.62 |
| ai_meta | 20616 | 20.62 |
| ai_other | 20616 | 20.62 |
| scroll_events | 20616 | 20.62 |
| month | 0 | 0.0 |

---

## fact_content_query_90d

- Rows: **2414248**
- Columns: **21**
- Memory: **545.67 MB**
- Duplicate Rows: **0**

### Missing Values

| Column | Missing | % |
|--------|---------|---|
| client_hash_id | 0 | 0.0 |
| content_hash_id | 0 | 0.0 |
| query_hash_id | 0 | 0.0 |
| query_char_count | 0 | 0.0 |
| query_token_count | 0 | 0.0 |
| window_start | 0 | 0.0 |
| window_end | 0 | 0.0 |
| impressions_90d | 0 | 0.0 |
| clicks_90d | 0 | 0.0 |
| impressions_last30 | 0 | 0.0 |
| clicks_last30 | 0 | 0.0 |
| impressions_prev30 | 0 | 0.0 |
| clicks_prev30 | 0 | 0.0 |
| avg_position_90d | 0 | 0.0 |
| avg_position_last30 | 530758 | 21.98 |
| avg_position_prev30 | 329420 | 13.64 |
| content_total_impressions_90d | 0 | 0.0 |
| content_visible_query_count | 0 | 0.0 |
| rare_query_count | 0 | 0.0 |
| rare_impressions_share | 0 | 0.0 |
| anonymized_impressions_share | 0 | 0.0 |

---

