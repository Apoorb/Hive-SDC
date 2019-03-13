/* 1 Hive Commands for :thea_bsm_core table*/
SELECT * FROM thea_bsm_core LIMIT 5;
SELECT COUNT(*) as Count_thea_bsm_core from thea_bsm_core;
SELECT MAX(TO_DATE(metadatarecordgeneratedat)) as MaxDate_thea_bsm_corexx FROM thea_bsm_core;
SELECT MIN(TO_DATE(metadatarecordgeneratedat)) as MinDate_thea_bsm_corexx FROM thea_bsm_core;

/* 2 Hive Commands for :thea_bsm_partii table*/
SELECT * FROM thea_bsm_partii LIMIT 5;
SELECT COUNT(*) as Count_thea_bsm_partii from thea_bsm_partii;

/* 3 Hive Commands for :thea_bsm_partii_crumbdata table*/
SELECT * FROM thea_bsm_partii_crumbdata LIMIT 5;
SELECT COUNT(*) as Count_thea_bsm_partii_crumbdata from thea_bsm_partii_crumbdata;

/* 4 Hive Commands for :thea_bsm_v5 table*/
SELECT * FROM thea_bsm_v5 LIMIT 5;
SELECT COUNT(*) as Count_thea_bsm_v5 from thea_bsm_v5;

/* 5 Hive Commands for :thea_mmitss table*/
SELECT * FROM thea_mmitss LIMIT 5;
SELECT COUNT(*) as Count_thea_mmitss from thea_mmitss;

/* 6 Hive Commands for :thea_spat table*/
SELECT * FROM thea_spat LIMIT 5;
SELECT COUNT(*) as Count_thea_spat from thea_spat;

/* 7 Hive Commands for :thea_spat_core table*/
SELECT * FROM thea_spat_core LIMIT 5;
SELECT COUNT(*) as Count_thea_spat_core from thea_spat_core;
SELECT MAX(TO_DATE(metadatarecordgeneratedat)) as MaxDate_thea_spat_corexx FROM thea_spat_core;
SELECT MIN(TO_DATE(metadatarecordgeneratedat)) as MinDate_thea_spat_corexx FROM thea_spat_core;

/* 8 Hive Commands for :thea_spat_intersectionstate_enabledlanes table*/
SELECT * FROM thea_spat_intersectionstate_enabledlanes LIMIT 5;
SELECT COUNT(*) as Count_thea_spat_intersectionstate_enabledlanes from thea_spat_intersectionstate_enabledlanes;

/* 9 Hive Commands for :thea_spat_intersectionstate_movementstate table*/
SELECT * FROM thea_spat_intersectionstate_movementstate LIMIT 5;
SELECT COUNT(*) as Count_thea_spat_intersectionstate_movementstate from thea_spat_intersectionstate_movementstate;

/* 10 Hive Commands for :wydot_alert_core table*/
SELECT * FROM wydot_alert_core LIMIT 5;
SELECT COUNT(*) as Count_wydot_alert_core from wydot_alert_core;
SELECT MAX(TO_DATE(metadatarecordgeneratedat)) as MaxDate_wydot_alert_core FROM wydot_alert_core;
SELECT MIN(TO_DATE(metadatarecordgeneratedat)) as MinDate_wydot_alert_core FROM wydot_alert_core;

/* 11 Hive Commands for :wydot_alert_v5 table*/
SELECT * FROM wydot_alert_v5 LIMIT 5;
SELECT COUNT(*) as Count_wydot_alert_v5 from wydot_alert_v5;

/* 12 Hive Commands for :wydot_bsm_core table*/
--SELECT TO_DATE(metadatarecordgeneratedat) FROM wydot_bsm_core LIMIT 40 OFFSET 74520490;
SELECT * FROM wydot_bsm_core SORT BY TO_DATE(metadataodereceivedat) DESC LIMIT 40;
SELECT COUNT(*) as Count_wydot_bsm_core from wydot_bsm_core;
SELECT MAX(TO_DATE(metadataodereceivedat)) as MaxDate_wydot_bsm_core FROM wydot_bsm_core;
SELECT MIN(TO_DATE(metadataodereceivedat)) as MinDate_wydot_bsm_core FROM wydot_bsm_core;

/* 13 Hive Commands for :wydot_bsm_partii table*/
SELECT * FROM wydot_bsm_partii LIMIT 5;
SELECT COUNT(*) as Count_wydot_bsm_partii from wydot_bsm_partii;

/* 14 Hive Commands for :wydot_bsm_partii_crumbdata table*/
SELECT * FROM wydot_bsm_partii_crumbdata LIMIT 5;
SELECT COUNT(*) as Count_wydot_bsm_partii_crumbdata from wydot_bsm_partii_crumbdata;

/* 15 Hive Commands for :wydot_bsm_v4 table*/
SELECT * FROM wydot_bsm_v4 LIMIT 5;
SELECT COUNT(*) as Count_wydot_bsm_v4 from wydot_bsm_v4;

/* 16 Hive Commands for :wydot_bsm_v5 table*/
SELECT * FROM wydot_bsm_v5 LIMIT 5;
SELECT COUNT(*) as Count_wydot_bsm_v5 from wydot_bsm_v5;

/* 17 Hive Commands for :wydot_rwis_atmos table*/
SELECT * FROM wydot_rwis_atmos LIMIT 5;
SELECT COUNT(*) as Count_wydot_rwis_atmos from wydot_rwis_atmos;
SELECT MAX(TO_DATE(utc)) as MaxDate_wydot_rwis_atmos FROM wydot_rwis_atmos;
SELECT MIN(TO_DATE(utc)) as MinDate_wydot_rwis_atmos FROM wydot_rwis_atmos;

/* 18 Hive Commands for :wydot_rwis_index table*/
SELECT * FROM wydot_rwis_index LIMIT 5;
SELECT COUNT(*) as Count_wydot_rwis_index from wydot_rwis_index;

/* 19 Hive Commands for :wydot_rwis_surface table*/
SELECT * FROM wydot_rwis_surface LIMIT 5;
SELECT COUNT(*) as Count_wydot_rwis_surface from wydot_rwis_surface;
SELECT MAX(TO_DATE(utc)) as MaxDate_wydot_rwis_surface FROM wydot_rwis_surface;
SELECT MIN(TO_DATE(utc)) as MinDate_wydot_rwis_surface FROM wydot_rwis_surface;

/* 20 Hive Commands for :wydot_segments_index table*/
SELECT * FROM wydot_segments_index LIMIT 5;
SELECT COUNT(*) as Count_wydot_segments_index from wydot_segments_index;

/* 21 Hive Commands for :wydot_speed_controllers table*/
SELECT * FROM wydot_speed_controllers LIMIT 5;
SELECT COUNT(*) as Count_wydot_speed_controllers from wydot_speed_controllers;

/* 22 Hive Commands for :wydot_speed_processed table*/
SELECT * FROM wydot_speed_processed LIMIT 5;
select from_unixtime(unix_timestamp(date_time,"MM/dd/yyyy hh:mm:ss"),"yyyy-MM-dd") from wydot_speed_processed Limit 10;
SELECT COUNT(*) as Count_wydot_speed_processed from wydot_speed_processed;
SELECT from_unixtime(MAX(unix_timestamp(date_time,"MM/dd/yyyy hh:mm:ss")),"yyyy-MM-dd") as MaxDate_wydot_speed_processed FROM wydot_speed_processed;
SELECT from_unixtime(MIN(unix_timestamp(date_time,"MM/dd/yyyy hh:mm:ss")),"yyyy-MM-dd") as MinDate_wydot_speed_processed FROM wydot_speed_processed;

/* 23 Hive Commands for :wydot_speed_sensors_index table*/
select * from  wydot_speed_sensors_index LIMIT 5;
SELECT COUNT(*) as Count_wydot_speed_sensors_index from wydot_speed_sensors_index;

/* 24 Hive Commands for :wydot_speed_signs_index table*/
select * from  wydot_speed_signs_index LIMIT 5;
SELECT COUNT(*) as Count_wydot_speed_signs_index from wydot_speed_signs_index;

/* 25 Hive Commands for :wydot_speed_unprocessed table*/
select * from  wydot_speed_unprocessed LIMIT 5;
SELECT COUNT(*) as Count_wydot_speed_unprocessed from wydot_speed_unprocessed;
SELECT MAX(TO_DATE(mountain)) as MaxDate_wydot_speed_unprocessed FROM wydot_speed_unprocessed;
SELECT MIN(TO_DATE(mountain)) as MinDate_wydot_speed_unprocessed FROM wydot_speed_unprocessed;

/* 26 Hive Commands for :wydot_tim_advisory table*/
select * from  wydot_tim_advisory LIMIT 5;
SELECT COUNT(*) as Count_wydot_tim_advisory from wydot_tim_advisory;

/* 27 Hive Commands for :wydot_tim_core table*/
select * from  wydot_tim_core LIMIT 5;
SELECT COUNT(*) as Count_wydot_tim_core from wydot_tim_core;
SELECT MAX(TO_DATE(metadatarecordgeneratedat)) as MaxDate_wydot_tim_core FROM wydot_tim_core;
SELECT MIN(TO_DATE(metadatarecordgeneratedat)) as MinDate_wydot_tim_core FROM wydot_tim_core;

/* 28 Hive Commands for :wydot_tim_path_offset_ll table*/
select * from  wydot_tim_path_offset_ll LIMIT 5;
SELECT COUNT(*) as Count_wydot_tim_path_offset_ll from wydot_tim_path_offset_ll;

/* 29 Hive Commands for :wydot_tim_path_offset_xy table*/
select * from  wydot_tim_path_offset_xy LIMIT 5;
SELECT COUNT(*) as Count_wydot_tim_path_offset_xy from wydot_tim_path_offset_xy;

/* 30 Hive Commands for :wydot_tim_v5 table*/
select * from  wydot_tim_v5 LIMIT 5;
SELECT COUNT(*) as Count_wydot_tim_v5 from wydot_tim_v5;

/* 31 Hive Commands for :wydot_tim_v6 table*/
select * from  wydot_tim_v6 LIMIT 5;
SELECT COUNT(*) as Count_wydot_tim_v6 from wydot_tim_v6;

/* 32 Hive Commands for :wydot_vlogs_query_summary table*/
SELECT * FROM  wydot_vlogs_query_summary LIMIT 5;
SELECT COUNT(*) as Count_wydot_vlogs_query_summary from wydot_vlogs_query_summary;
SELECT MAX(TO_DATE(enddate)) as MaxDate_wydot_vlogs_query_summary FROM wydot_vlogs_query_summary;
SELECT MIN(TO_DATE(enddate)) as MinDate_wydot_vlogs_query_summary FROM wydot_vlogs_query_summary;

/* 33 Hive Commands for :wydot_vsl table*/
SELECT * FROM  wydot_vsl LIMIT 5;
SELECT COUNT(*) as Count_wydot_vsl from wydot_vsl;
SELECT MAX(TO_DATE(utc)) as MaxDate_wydot_vsl FROM wydot_vsl;
SELECT MIN(TO_DATE(utc)) as MinDate_wydot_vsl FROM wydot_vsl;

