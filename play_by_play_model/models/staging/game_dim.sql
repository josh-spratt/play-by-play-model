SELECT DISTINCT
	md5(home_team||away_team||game_date)::varchar game_sk
	,home_team::varchar home_team_abbr
	,away_team::varchar away_team_abbr
	,season_type::varchar season_type
	,week::numeric "week"
	,game_date::date game_date
	,season::numeric season
	,try_strptime(start_time,'%m/%d/%y, %H:%M:%S') start_time
	,stadium::varchar stadium
	,weather::varchar weather
	,location::varchar "location"
	,result::numeric result
	,total::numeric total_score
	,spread_line::numeric spread_line
	,total_line::numeric total_line
	,CASE WHEN div_game = 1 THEN TRUE ELSE FALSE END div_game
	,roof::varchar roof_type
	,surface::varchar surface_type
	,temp::numeric temperature
	,wind::numeric wind_speed
	,home_coach::varchar home_coach
	,away_coach::varchar awaycoach
	,stadium_id::varchar stadium_id
	,game_stadium::varchar game_stadium
	,CASE WHEN home_opening_kickoff = 1 THEN TRUE ELSE FALSE END home_opening_kickoff
FROM nfl_stg.base_play_by_play_2023