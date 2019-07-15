--nba_shots.pig: transforms shots_dataframe.csv for a Hive table

shots = LOAD 'shots_dataframe.csv' USING PigStorage(',');

nba_shots = FOREACH shots GENERATE
   (chararray) $7 AS player_position,
   (chararray) $3 AS home,
   (float) $5 AS loc_x,
   (chararray) $4 AS home_team,
   (chararray) $11 AS shot_type,
   (int) $8 AS points,
   (chararray) $0 AS away_team,
   (float) $6 AS loc_y,
   (chararray) $12 AS time,
   (chararray) $2 AS game_date,
   (chararray) $10 AS shooter,
   (int) $9 AS quarter,
   (chararray) $1 AS outcome;

--Store the results in the folder 'nba_shots' in the HDFS home directory
STORE nba_shots INTO 'nba_shots/';
