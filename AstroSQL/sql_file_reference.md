# SQL COMMANDS USED TO CREATE THE test.db DATABASE AND ADD DATA

    CREATE TABLE images(image_id TEXT NOT NULL PRIMARY KEY,ra_cen REAL,dec_cen REAL, date TEXT, time TEXT);

    CREATE TABLE spectral_categories(spectral_type TEXT NOT NULL PRIMARY KEY,T_eff REAL);

    CREATE TABLE stars(star_id TEXT NOT NULL PRIMARY KEY, image_id TEXT, ra REAL, dec REAL, v_mag REAL, spectral_type TEXT, FOREIGN KEY(image_id) REFERENCES images(image_id), FOREIGN KEY(spectral_type) REFERENCES spectral_categories(spectral_type));


    INSERT INTO images VALUES('145-33-01',145.2,-33.1, '20130321','1117');
    INSERT INTO images VALUES('146-33-01',146.2,-33.1, '20130321','1152');
    INSERT INTO images VALUES('147-33-01',147.2,-33.1, '20130321','1229');
    INSERT INTO images VALUES('145-34-01',145.2,-34.1, '20130322','1312');
    INSERT INTO images VALUES('146-34-01',146.2,-34.1, '20130322','1117');
    INSERT INTO images VALUES('147-34-01',147.2,-34.1, '20130322','1117');

    INSERT INTO spectral_categories VALUES('O',50000);
    INSERT INTO spectral_categories VALUES('B',28000);
    INSERT INTO spectral_categories VALUES('A',10000);
    INSERT INTO spectral_categories VALUES('F',7500);
    INSERT INTO spectral_categories VALUES('G',6000);
    INSERT INTO spectral_categories VALUES('K',5000);
    INSERT INTO spectral_categories VALUES('M',3500);

    INSERT INTO stars VALUES('HIP29807','146-34-01',146.12,-34.32,6.78,'O');
    INSERT INTO stars VALUES('HIP30973','146-33-01',146.33,-32.91,7.98,'G');
    INSERT INTO stars VALUES('HD35294','145-33-01',144.82,-33.21,11.56,'O');
    INSERT INTO stars VALUES('HD269324','145-33-01',145.22,-33.21,12.67,'M');
    INSERT INTO stars VALUES('HD269334','145-33-01',145.28,-33.17,12.68,'M');
    INSERT INTO stars VALUES('HD49091','146-34-01',145.82,-34.34,9.99,'M');
    INSERT INTO stars VALUES('HD49126','146-34-01',145.82,-34.41,13.01,'M');
    INSERT INTO stars VALUES('HD169334','146-34-01',146.50,-33.73,12.81,'B');
    INSERT INTO stars VALUES('1252BT14','146-33-01',145.90,-33.24,10.02,'M');
    INSERT INTO stars VALUES('1252BT12','146-34-01',146.26,-34.45,12.98,'M');
    INSERT INTO stars VALUES('1252BT18','147-34-01',146.66,-33.84,8.42,'F');
    INSERT INTO stars VALUES('HD48765','147-34-01',146.76,-33.56,8.45,'M');
    INSERT INTO stars VALUES('HD24670','147-34-01',146.62,-34.34,9.07,'M');

# SQLite – STARTING, QUITTING AND METACOMMANDS

starting:
    sqlite3 test.db

quitting:
    .exit
    .quit


metacommands:
    .help
    .tables
    .schema
    .show
    .header on
    .mode column

# SQL COMMANDS USED TO EXTRACT DATA FROM THE test.db DATABASE

    SELECT * FROM stars;
    .mode columns
    SELECT * FROM spectral_categories;
    SELECT * FROM images;
    SELECT * FROM stars WHERE image_id = '146-34-01';
    SELECT * FROM stars WHERE spectral_type = 'O' AND image_id = '146-34-01';
    SELECT * FROM stars WHERE dec > -33 OR image_id = '146-34-01';
    SELECT * FROM stars where image_id LIKE '145%';
    SELECT * FROM stars WHERE image_id = '146-34-01' ORDER by ra;
    SELECT star_id, spectral_type FROM stars;
    SELECT star_id, v_mag FROM stars WHERE image_id= '146-34-01' ORDER by v_mag;
    SELECT ra, dec, star_id FROM stars WHERE image_id= '146-34-01' ORDER by ra, dec;
    SELECT * FROM stars LIMIT 3;
    SELECT max(ra), min(ra) FROM stars;
    SELECT AVG(dec) as dec_avg FROM stars WHERE image_id= '146-34-01';
    SELECT spectral_type, AVG(v_mag) as v_mag_avg FROM stars GROUP BY spectral_type;

outputting the data:
    .mode csv
    .output stars.csv
    SELECT * FROM stars;
    .output stdout
    .mode columns
