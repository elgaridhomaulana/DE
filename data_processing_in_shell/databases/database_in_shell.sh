# sql2csv
# sql2csv untuk query sql dan mengubahnya ke csv
sql2csv -h

# query dari database
sql2csv --db "sqlite:///SpotifyDatabase.db" \
        --query "SELECT * FROM Spotify_Popularity" \
        > Spotify_Popularity.csv

# csvsql
csvsql -h

# apply SQL ke csv lokal
csvsql --query "SELECT * FROM Spotify_MusicAttributes LIMIT 1" \
    Spotify_MusicAttributes.csv

# pushing data back to database
csvsql --db "sqlite:///SpotifyDatabase.db" \
        --insert Spotify_MusicAttributes.csv

#Example
# Store SQL for querying from SQLite database 
sqlquery_pull="SELECT * FROM SpotifyMostRecentData"

# Apply SQL to save table as local file 
sql2csv --db "sqlite:///SpotifyDatabase.db" --query "$sqlquery_pull" > SpotifyMostRecentData.csv

# Store SQL for UNION of the two local CSV files
sqlquery_union="SELECT * FROM SpotifyMostRecentData UNION ALL SELECT * FROM Spotify201812"

# Apply SQL to union the two local CSV files and save as local file
csvsql 	--query "$sqlquery_union" SpotifyMostRecentData.csv Spotify201812.csv > UnionedSpotifyData.csv

# Push UnionedSpotifyData.csv to database as a new table
csvsql --db "sqlite:///SpotifyDatabase.db" --insert UnionedSpotifyData.csv