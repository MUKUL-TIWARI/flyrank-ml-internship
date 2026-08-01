# FlyRank Data Dictionary

## dim_clients

| Column | Type |
|--------|------|
| client_hash_id | VARCHAR |
| is_active | BOOLEAN |
| has_gsc_access | BOOLEAN |
| has_ga4_access | BOOLEAN |
| access_profile | VARCHAR |
| client_created_date | DATE |
| client_updated_date | DATE |
| gsc_data_start | DATE |
| ga4_data_start | DATE |

## dim_content

| Column | Type |
|--------|------|
| client_hash_id | VARCHAR |
| content_hash_id | VARCHAR |
| keyword_hash_id | VARCHAR |
| url_hash_id | VARCHAR |
| keyword_char_count | BIGINT |
| keyword_token_count | BIGINT |
| url_char_count | BIGINT |
| content_created_date | DATE |
| content_updated_date | DATE |
| content_type | VARCHAR |
| search_volume | BIGINT |
| competition | DOUBLE |
| competition_level | VARCHAR |
| cpc | DOUBLE |
| main_intent | VARCHAR |
| backlinks | BIGINT |
| category_count | BIGINT |
| keyword_created_date | DATE |
| provider_used | VARCHAR |
| model_used | VARCHAR |
| char_count | BIGINT |
| word_count | BIGINT |
| last_optimized_date | DATE |
| optimization_eligible_date | DATE |
| is_published | BOOLEAN |
| is_deleted | BOOLEAN |

## fact_content_daily_performance

| Column | Type |
|--------|------|
| report_date | DATE |
| client_hash_id | VARCHAR |
| content_hash_id | VARCHAR |
| client_has_gsc | BOOLEAN |
| client_has_ga4 | BOOLEAN |
| gsc_data_available | BOOLEAN |
| ga4_data_available | BOOLEAN |
| gsc_impressions | BIGINT |
| gsc_clicks | BIGINT |
| gsc_sum_position | BIGINT |
| gsc_avg_position | DOUBLE |
| ga4_pageviews | BIGINT |
| ga4_sessions | BIGINT |
| ga4_users | BIGINT |
| ga4_engaged_sessions | BIGINT |
| ga4_total_engagement_sec | BIGINT |
| sessions_organic | BIGINT |
| sessions_direct | BIGINT |
| sessions_referral | BIGINT |
| sessions_social | BIGINT |
| sessions_paid | BIGINT |
| sessions_ai | BIGINT |
| ai_chatgpt | BIGINT |
| ai_perplexity | BIGINT |
| ai_gemini | BIGINT |
| ai_copilot | BIGINT |
| ai_claude | BIGINT |
| ai_meta | BIGINT |
| ai_other | BIGINT |
| scroll_events | BIGINT |
| month | VARCHAR |

## fact_content_query_90d

| Column | Type |
|--------|------|
| client_hash_id | VARCHAR |
| content_hash_id | VARCHAR |
| query_hash_id | VARCHAR |
| query_char_count | BIGINT |
| query_token_count | BIGINT |
| window_start | DATE |
| window_end | DATE |
| impressions_90d | BIGINT |
| clicks_90d | BIGINT |
| impressions_last30 | BIGINT |
| clicks_last30 | BIGINT |
| impressions_prev30 | BIGINT |
| clicks_prev30 | BIGINT |
| avg_position_90d | DOUBLE |
| avg_position_last30 | DOUBLE |
| avg_position_prev30 | DOUBLE |
| content_total_impressions_90d | BIGINT |
| content_visible_query_count | BIGINT |
| rare_query_count | BIGINT |
| rare_impressions_share | DOUBLE |
| anonymized_impressions_share | DOUBLE |

