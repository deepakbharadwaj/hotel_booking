CREATE TABLE IF NOT EXISTS `hotel` (
  `hid` int(5) NOT NULL,
  `name` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `zip` varchar(10) NOT NULL,
  `imgfolder` varchar(255) NOT NULL
);

INSERT INTO `hotel` (`hid`, `name`, `phone`, `email`, `zip` ) VALUES (1, 'Hotel1', '1111111', '1@hotel.com', '11');
INSERT INTO `hotel` (`hid`, `name`, `phone`, `email`, `zip` ) VALUES (2, 'Hotel2', '2222222', '2@hotel.com', '22');
INSERT INTO `hotel` (`hid`, `name`, `phone`, `email`, `zip` ) VALUES (3, 'Hotel3', '3333333', '3@hotel.com', '33');
INSERT INTO `hotel` (`hid`, `name`, `phone`, `email`, `zip` ) VALUES (4, 'Hotel4', '4444444', '4@hotel.com', '44');
INSERT INTO `hotel` (`hid`, `name`, `phone`, `email`, `zip` ) VALUES (5, 'Hotel5', '5555555', '5@hotel.com', '55');

ALTER TABLE `hotel` ADD PRIMARY KEY (`hid`);
ALTER TABLE `hotel` MODIFY `hid` int(5) NOT NULL AUTO_INCREMENT;



CREATE TABLE IF NOT EXISTS `room` (
  `rid` int(5) NOT NULL,
  `hid` int(5) NOT NULL,
  `rtype` varchar(50) NOT NULL,
  `rnumber` varchar(5) NOT NULL,
  `price` varchar(50) NOT NULL,
  `image` varchar(255) NOT NULL
);

INSERT INTO `room` (`rid`, `hid`, `rtype`, `rnumber`, `price` ) VALUES (1, 1, 'type1', '101', '1000');
INSERT INTO `room` (`rid`, `hid`, `rtype`, `rnumber`, `price` ) VALUES (2, 1, 'type2', '102', '2000');
INSERT INTO `room` (`rid`, `hid`, `rtype`, `rnumber`, `price` ) VALUES (3, 2, 'type3', '103', '3000');
INSERT INTO `room` (`rid`, `hid`, `rtype`, `rnumber`, `price` ) VALUES (4, 2, 'type4', '104', '4000');
INSERT INTO `room` (`rid`, `hid`, `rtype`, `rnumber`, `price` ) VALUES (5, 3, 'type5', '105', '5000');
INSERT INTO `room` (`rid`, `hid`, `rtype`, `rnumber`, `price` ) VALUES (6, 4, 'type6', '106', '6000');
INSERT INTO `room` (`rid`, `hid`, `rtype`, `rnumber`, `price` ) VALUES (7, 4, 'type7', '107', '7000');
INSERT INTO `room` (`rid`, `hid`, `rtype`, `rnumber`, `price` ) VALUES (8, 5, 'type8', '108', '8000');

ALTER TABLE `room` ADD PRIMARY KEY (`rid`);
ALTER TABLE `room` MODIFY `rid` int(5) NOT NULL AUTO_INCREMENT;
