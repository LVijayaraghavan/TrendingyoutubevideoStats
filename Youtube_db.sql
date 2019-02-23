

drop database youtube;
CREATE DATABASE youtube;
USE youtube;


#drop table youtube_video;
-- Create tables for raw data to be loaded into
CREATE TABLE youtube_video(
record_no INTEGER AUTO_INCREMENT PRIMARY KEY,
video_id VARCHAR (1000) ,
title TEXT ,
trending_date DATE,
category VARCHAR (1000),
publish_date DATE,
views INT,
comment_count INT,
likes INT,
dislikes INT
) DEFAULT CHARSET= utf8mb4;

CREATE TABLE youtube_summary(
category VARCHAR (1000) PRIMARY KEY,
views bigint, 
comment_count bigint,
likes bigint,
dislikes bigint,
views_per_comment bigint,
views_per_likes bigint,
views_per_dislikes bigint 
);
