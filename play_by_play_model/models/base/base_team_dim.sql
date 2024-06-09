WITH base AS (
    SELECT
        *
    FROM {{ source('fantasy_db', 'team_data') }}
)

SELECT
    team_id
    , team_name
    , team_abbr
    , team_nick
    , team_conf
    , team_division
    , team_color
    , team_color2
    , team_color3
    , team_color4
    , team_logo_wikipedia
    , team_logo_espn
    , team_wordmark
    , team_conference_logo
    , team_league_logo
    , team_logo_squared
FROM base
