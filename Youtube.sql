-- Create and use Youtube
CREATE DATABASE Youtube;
USE Youtube;

-- Create tables for raw data to be loaded into
CREATE TABLE you_video(
video_id VARCHAR (30) PRIMARY KEY,
trending_date DATE,
title VARCHAR (60),
description VARCHAR (1000),
catergory VARCHAR (1000),
publish_date DATE,
views INT,
comment_count INT,
likes INT,
dislike INT
);

CREATE TABLE Youtube_Summary(
category VARCHAR (1000) PRIMARY KEY,
views INT, 
comments INT,
likes INT,
dislikes INT,
comeent_per_views INT,
likes_per_views INT,
dislikes_per_views INT 
);





 
 
