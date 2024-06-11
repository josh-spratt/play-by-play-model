SELECT DISTINCT
	md5(home_team||away_team||game_date) game_sk
	,home_team
	,away_team
	,season_type
	,week
	,game_date
	,season
	,start_time
	,stadium
	,weather
	,location
	,result
	,total
	,spread_line
	,total_line
	,div_game
	,roof
	,surface
	,temp
	,wind
	,home_coach
	,away_coach
	,stadium_id
	,game_stadium
	,home_opening_kickoff
FROM nfl_stg.base_play_by_play_2023