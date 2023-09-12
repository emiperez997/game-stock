-- COMPANIES
-- INSERT INTO companies (name, foundation_year, country)
-- VALUES
-- ('Konami', 1969, 'Japan'),
-- ('Capcom', 1979, 'Japan'),
-- ('Square Enix', 2003, 'Japan'),
-- ('Ubisoft', 1986, 'France'),
-- ('Rockstar Games', 1998, 'United States'),
-- ('Electronic Arts', 1982, 'United States'),
-- ('Activision', 1979, 'United States'),
-- ('Sony Interactive Entertainment', 1993, 'Japan'),
-- ('Nintendo', 1889, 'Japan'),
-- ('Microsoft', 1975, 'United States'),
-- ('Sega', 1960, 'Japan'),
-- ('Bandai Namco', 2006, 'Japan');

-- SELECT * FROM companies;

-- GENRES
-- INSERT INTO genres (name, description)
-- VALUES 
-- ('Action', 'An action game is a video game genre that emphasizes physical challenges, including hand–eye coordination and reaction time.'),
-- ('Adventure', 'An adventure game (rarely called a quest game) is a video game genre in which the player assumes the role of a protagonist in an interactive story, driven by exploration and/or puzzle-solving.'),
-- ('Horror', 'A horror game is a video game genre centered on horror fiction and typically designed to scare the player. The term may also be used to describe tabletop games with horror fiction elements.'),
-- ('Survival Horror', 'Survival horror is a subgenre of horror games. Although combat can be part of the gameplay, the player is made to feel less in control than in typical action games through limited ammunition or weapons, health, speed, and vision, or through various obstructions of the player`s interaction with the game mechanics.'),
-- ('RPG', 'A role-playing video game, commonly referred to as a role-playing game (RPG) or computer role-playing game (CRPG), is a video game genre where the player controls the actions of a character (or several party members) immersed in some well-defined world, usually involving some form of character development by way of recording statistics.')

-- CONSOLES
-- INSERT INTO consoles (name, description, year)
-- VALUES
-- ('Playstation 1', 'The PlayStation is a home video game console developed and marketed by Sony Computer Entertainment. It was first released on 3 December 1994 in Japan, on 9 September 1995 in North America, on 29 September 1995 in Europe, and on 15 November 1995 in Australia, and was the first of the PlayStation lineup of video game consoles.', 1994),
-- ('Playstation 2', 'The PlayStation 2 is a home video game console developed and marketed by Sony Computer Entertainment. It was first released in Japan on 4 March 2000, in North America on 26 October 2000, in Europe on 24 November 2000, and Australia on 24 November 2000. It is the successor to the original PlayStation, as well as the second installment in the PlayStation console line-up.', 2000),
-- ('Playstation 3', 'The PlayStation 3 (PS3) is a home video game console developed by Sony Computer Entertainment. It is the successor to PlayStation 2, and is part of the PlayStation brand of consoles. It was first released on November 11, 2006 in Japan, November 17, 2006 in North America, and March 23, 2007 in Europe and Australia. The PlayStation 3 competed primarily against Microsoft`s Xbox 360 and Nintendo`s Wii as part of the seventh generation of video game consoles.', 2006),
-- ('PSP', 'The PlayStation Portable (PSP) is a handheld game console developed and marketed by Sony Computer Entertainment. It was first released in Japan on December 12, 2004, in North America on March 24, 2005, and in PAL regions on September 1, 2005, and is the first handheld installment in the PlayStation line of consoles. As a seventh generation console, the PSP primarily competed with the Nintendo DS.', 2004),
-- ('Microsoft Windows', 'Microsoft Windows, commonly referred to as Windows, is a group of several proprietary graphical operating system families, all of which are developed and marketed by Microsoft. Each family caters to a certain sector of the computing industry. Active Microsoft Windows families include Windows NT and Windows IoT; these may encompass subfamilies, e.g. Windows Server or Windows Embedded Compact (Windows CE). Defunct Microsoft Windows families include Windows 9x, Windows Mobile and Windows Phone.', 1985),
-- ('Xbox 360', 'The Xbox 360 is a home video game console developed by Microsoft. As the successor to the original Xbox, it is the second console in the Xbox series. It competed with Sony`s PlayStation 3 and Nintendo`s Wii as part of the seventh generation of video game consoles. It was officially unveiled on MTV on May 12, 2005, with detailed launch and game information announced later that month at the 2005 Electronic Entertainment Expo.', 2005),
-- ('Nintendo Gamecube', 'The Nintendo GameCube is a home video game console released by Nintendo in Japan and North America in 2001 and Europe and Australia in 2002. The sixth-generation console is the successor to the Nintendo 64 and competed with Sony Computer Entertainment`s PlayStation 2 and Microsoft`s Xbox.', 2001);


-- GAMES
-- INSERT INTO games (title, year, director, company_id, images, videos, description)
-- VALUES
-- 1  ('Silent HIll', 1999, 'Keiichiro Toyama', 1, ARRAY['https://th.bing.com/th/id/R.1c750515fbab3ab0cb46ce40aea6ffa2?rik=DG4e1a%2bs0T79UA&riu=http%3a%2f%2f3.bp.blogspot.com%2f-H6-Nt2CDVvU%2fUEts0HhXYyI%2fAAAAAAAABRk%2fEEiN7-EOlGk%2fs1600%2fSilent_Hill_capa.jpg&ehk=5fmEtvDJtl1t2h%2bG1nKoOGY8rXzxCoAp9DMAAhfkSMc%3d&risl=&pid=ImgRaw&r=0', 'https://playstationinside.fr/wp-content/uploads/2021/01/sh1.jpg', 'https://www.bing.com/images/search?view=detailV2&ccid=p3FPFQM0&id=DCAED1A5A7399E1C269F3BB9FD33E8E20A4637C5&thid=OIP.p3FPFQM0h4741pDiRQTIAwHaEK&mediaurl=https%3a%2f%2f3.bp.blogspot.com%2f-YG-HaCUdxLI%2fVtSQoJPzD0I%2fAAAAAAAAAu8%2f11EnbNJuo2U%2fs1600%2fSilent-Hill.jpg&cdnurl=https%3a%2f%2fth.bing.com%2fth%2fid%2fR.a7714f150334878ef8d690e24504c803%3frik%3dxTdGCuLoM%252f25Ow%26pid%3dImgRaw%26r%3d0&exph=900&expw=1600&q=Silent+Hill+1+PS1&simid=608011896148736693&FORM=IRPRST&ck=9679FD751AD1E8659B08B64BB55B3A44&selectedIndex=9&ajaxhist=0&ajaxserp=0'], ARRAY['https://youtu.be/TdZuQeM2T8w?si=FXJboX1vkiyBmbnB'], 'Silent Hill is a 1999 survival horror game developed by Team Silent, a group in Konami Computer Entertainment Tokyo and published by Konami. The first installment in the video game series Silent Hill, the game was released from February to July, originally for the PlayStation.'),
-- 2 ('Silent HIll 2', 2001, 'Masashi Tsuboyama', 1, ARRAY['https://th.bing.com/th/id/OIP.eELOv8Nacl_TEof8P6fvDAAAAA?pid=ImgDet&rs=1', 'https://th.bing.com/th/id/R.1390caaa7f627046ffaa95c9eefd0992?rik=Tuo6PKZv3MBzSg&pid=ImgRaw&r=0&sres=1&sresct=1', 'https://cdn.mos.cms.futurecdn.net/a72677986b59ec44ff019a981f74322a.jpg'], ARRAY['https://youtu.be/4LCl2_DK6QU?si=He2kLiEPkHY_4XZB'], 'Silent Hill 2 is the second installment in the Silent Hill survival horror series and the first game of the series to be released for Sony PlayStation 2. The game was developed by Team Silent and published by Konami.'),
-- 3 ('Final Fantasy Crisis Core', 2007, 'Hajime Tabata', 2, ARRAY['https://th.bing.com/th/id/R.fde701ee9cb534fdd74c2982ca11ad39?rik=6uTcwNowARI2JA&pid=ImgRaw&r=0', 'https://i.ytimg.com/vi/Dy871WOpxlA/maxresdefault.jpg', 'https://i.ytimg.com/vi/8NbQW0u7ios/maxresdefault.jpg'], ARRAY['https://www.youtube.com/watch?v=zDrQRRUfbxw'], 'Crisis Core: Final Fantasy VII is an action role-playing game developed and published by Square Enix for the PlayStation Portable. First released in 2007, the game is a prequel to the 1997 video game Final Fantasy VII and is a part of the metaseries Compilation of Final Fantasy VII, which includes other products related to the original game.'),
-- 4 ('Far Cry 2', 2008, 'Clint Hocking', 3, ARRAY['https://th.bing.com/th/id/R.e9731d031c1b65af86d0ac237fed2905?rik=JDLdbFaMydgCtw&riu=http%3a%2f%2fwww.gamecash.fr%2fmedias%2ffar-cry-2-e676.jpg&ehk=6QFKoRAOQfIz%2f0Ja84aNnd%2bqaZK7aT3kIVNiwLjPDH0%3d&risl=&pid=ImgRaw&r=0', 'https://th.bing.com/th/id/R.254ae513b71e5e77da027540479e4cac?rik=fnPGaixWRDTfEw&pid=ImgRaw&r=0', 'https://i.ytimg.com/vi/0XqmxmONanc/maxresdefault.jpg'], ARRAY['https://www.youtube.com/watch?v=m-7m4vtn-eM'], 'Far Cry 2 is a 2008 first-person shooter developed by Ubisoft Montreal and published by Ubisoft for Microsoft Windows, PlayStation 3 and Xbox 360. A top-down shooter version for mobile phones was developed and published by Gameloft. It is the second mainline entry in the Far Cry series. Set in a fictional African country engulfed in civil war, the storyline follows a mercenary who is assigned to kill the Jackal, a weapons dealer inflaming the conflict.'),
-- 5 ('Resident Evil 4', 2005, 'Shinji Mikami', 4, ARRAY['https://th.bing.com/th/id/R.9e19e336622d012dc8e996690745c559?rik=zhxMJdTmBgbyXg&riu=http%3a%2f%2fimages1.fanpop.com%2fimages%2fimage_uploads%2fResident-Evil-4-resident-evil-894834_1280_1024.jpg&ehk=1CNlnYBNju0LP3IKvzRZE2nxcGPm9OUrqd0XrGzBJxE%3d&risl=&pid=ImgRaw&r=0', 'https://www.giantbomb.com/a/uploads/original/1/10354/2769656-resident_evil_4_ultimate_hd_edition-2448037.jpg', 'https://1.bp.blogspot.com/_vYk45ep4ZG0/TGhhjmwEN0I/AAAAAAAAARo/zXFC_kn3sPE/s1600/3520i0m.jpg'], ARRAY['https://www.youtube.com/watch?v=JpSOccC5sV0'], 'Resident Evil 4 is a survival horror game developed and published by Capcom for the GameCube in 2005. Players control special agent Leon S. Kennedy who is on a mission to rescue the US president`s daughter, Ashley Graham, who has been kidnapped by a religious cult in rural Spain.');

-- SELECT * FROM games
-- LEFT JOIN companies ON games.company_id = companies.company_id;

-- GAME GENRES
-- INSERT INTO game_genres (game_id, genre_id)
-- VALUES
-- (1, 3), -- Silent Hill - Horror
-- (1, 4), -- Silent Hill - Survival Horror 
-- (2, 3), -- Silent Hill 2 - Horror
-- (2, 4), -- Silent Hill 2 - Survival Horror
-- (3, 2), -- Final Fantasy Crisis Core - Adventure
-- (3, 5), -- Final Fantasy Crisis Core - Role-playing
-- (4, 1), -- Far cry 2 - Action
-- (4, 2),-- Far cry 2 - Adventure
-- (5, 1), -- Resident Evil 4 - Action
-- (5, 4); -- Resident Evil 4 -  Survival Horror

-- GAME CONSOLES
-- INSERT INTO game_consoles (game_id, console_id)
-- VALUES
-- (1, 1), -- Silent Hill - Playstation 1
-- (2, 2), -- Silent Hill 2 - Playstation 2
-- (2, 5), -- Silent Hill 2 - Microsoft Windows
-- (3, 4), -- Final Fantasy Crisis Core - PSP
-- (4, 3), -- Far cry 2 - Playstation 3
-- (4, 5), -- Far cry 2 - Microsoft Windows
-- (4, 6), -- Far cry 2 - Xbox 360
-- (5, 2), -- Resident Evil 4 - Playstation 2
-- (5, 3), -- Resident Evil 4 - Playstation 3
-- (5, 5), -- Resident Evil 4 - Microsoft Windows
-- (5, 6), -- Resident Evil 4 - Xbox 360
-- (5, 7); -- Resident Evil 4 - Nintendo Gamecube