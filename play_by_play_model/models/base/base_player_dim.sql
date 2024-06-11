WITH base AS (
    SELECT
        *
    FROM {{ source('nfl_stg', 'player_data') }}
)

SELECT
    gsis_id player_id -- this seems to be the id used in the PBP data
    , display_name full_name
    , first_name
    , last_name
    , suffix
    , short_name
    -- , football_name (too many name fields already)
    -- , esb_id
    , birth_date
    , college_name
    , position_group
    , position
    , jersey_number
    , height
    , weight
    , years_of_experience
    -- , team_abbr (join out to team_dim)
    -- , team_seq (join out to team_dim)
    , current_team_id team_id
    -- , gsis_it_id (not sure what these are, couldn't find much info, can add later if needed)
    -- , smart_id (not sure what these are, couldn't find much info, can add later if needed)
    , headshot headshot_url
    -- , entry_year (dupe of rookie_year)
    , rookie_year
    , draft_club draft_team_abbr --Replace with team_id later on
    , draft_number
    , college_conference
    , status
    , status_description_abbr
    , status_short_description
    -- , uniform_number (jersey_number is a more complete column)
    -- , draft_round (mostly null)
    -- , season (mostly null)
FROM base
