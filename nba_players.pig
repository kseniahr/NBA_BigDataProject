--nba_players.pig: transforms players_dataframe.csv for a Hive table

players = LOAD 'players_dataframe.csv' USING PigStorage(',');

nba_players = FOREACH players GENERATE
   (int) $0 AS player_id,
   (int) $1 AS jersey_number,
   (chararray) $2 AS position,
   (chararray) $3 AS birthdate,
   (int) $4 AS age,
   (chararray) $5 AS rookie,
   (int) $6 AS team_id,
   (chararray) $7 AS team_abbr,
   (chararray) $8 AS team_city,
   (chararray) $9 AS team_name,
   (int) $10 AS games_played,
   (int) $11 AS fg2_pt_att,
   (int) $12 AS fg2_pt_made,
   (int) $13 AS fg3_pt_att,
   (int) $14 AS fg3_pt_made,
   (int) $15 AS ft_att,
   (int) $16 AS ft_made,
   (chararray) $17 AS full_name;

--Store the results in the folder 'nba_players' in the HDFS home directory
STORE nba_players INTO 'nba_players/';
