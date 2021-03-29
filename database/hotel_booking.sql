SET time_zone = '+00:00';

CREATE TABLE IF NOT EXISTS `hotel` (
  `hid` int(5) NOT NULL,
  `name` varchar(50) NOT NULL,
  `phone` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `zip` varchar(10) NOT NULL,
  `imgfolder` varchar(255),
  PRIMARY KEY (`hid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
AUTO_INCREMENT=1;

INSERT INTO `hotel` (`hid`, `name`, `phone`, `email`, `zip` ) VALUES (1, 'Hotel1', '1111111', '1@hotel.com', '11');
INSERT INTO `hotel` (`hid`, `name`, `phone`, `email`, `zip` ) VALUES (2, 'Hotel2', '2222222', '2@hotel.com', '22');
INSERT INTO `hotel` (`hid`, `name`, `phone`, `email`, `zip` ) VALUES (3, 'Hotel3', '3333333', '3@hotel.com', '33');
INSERT INTO `hotel` (`hid`, `name`, `phone`, `email`, `zip` ) VALUES (4, 'Hotel4', '4444444', '4@hotel.com', '44');
INSERT INTO `hotel` (`hid`, `name`, `phone`, `email`, `zip` ) VALUES (5, 'Hotel5', '5555555', '5@hotel.com', '55');

ALTER TABLE `hotel` MODIFY `hid` int(5) NOT NULL AUTO_INCREMENT;

CREATE TABLE IF NOT EXISTS `room` (
  `rid` int(5) NOT NULL,
  `hid` int(5) NOT NULL,
  `rtype` varchar(50) NOT NULL,
  `rnumber` varchar(5) NOT NULL,
  `price` varchar(50) NOT NULL,
  `image` varchar(255),
  PRIMARY KEY (`rid`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
AUTO_INCREMENT=1;

INSERT INTO `room` (`rid`, `hid`, `rtype`, `rnumber`, `price` ) VALUES (1, 1, 'type1', '101', '1000');
INSERT INTO `room` (`rid`, `hid`, `rtype`, `rnumber`, `price` ) VALUES (2, 1, 'type2', '102', '2000');
INSERT INTO `room` (`rid`, `hid`, `rtype`, `rnumber`, `price` ) VALUES (3, 2, 'type3', '103', '3000');
INSERT INTO `room` (`rid`, `hid`, `rtype`, `rnumber`, `price` ) VALUES (4, 2, 'type4', '104', '4000');
INSERT INTO `room` (`rid`, `hid`, `rtype`, `rnumber`, `price` ) VALUES (5, 3, 'type5', '105', '5000');
INSERT INTO `room` (`rid`, `hid`, `rtype`, `rnumber`, `price` ) VALUES (6, 4, 'type6', '106', '6000');
INSERT INTO `room` (`rid`, `hid`, `rtype`, `rnumber`, `price` ) VALUES (7, 4, 'type7', '107', '7000');
INSERT INTO `room` (`rid`, `hid`, `rtype`, `rnumber`, `price` ) VALUES (8, 5, 'type8', '108', '8000');

ALTER TABLE `room` MODIFY `rid` int(5) NOT NULL AUTO_INCREMENT;

CREATE TABLE IF NOT EXISTS `bookings` (
  `bid` int(5) NOT NULL,
  `rid` int(5) NOT NULL,
  `from` date NOT NULL,
  `to` date NOT NULL,
  `cname` varchar(20) NOT NULL,
  `rname` varchar(20) NOT NULL,
  PRIMARY KEY (`bid`)
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin
AUTO_INCREMENT=1;

ALTER TABLE `bookings` MODIFY `bid` int(5) NOT NULL AUTO_INCREMENT;

INSERT INTO `bookings` (`bid`,`rid`,`from`,`to`,`cname`,`rname`) VALUES (1,1,'2020-01-01','2020-01-05', 'Customer1', 'Receptioninst'),
(2,1,'2020-01-09','2020-01-10', 'Customer1', 'Receptioninst'),
(3,1,'2020-02-01','2020-02-05', 'Customer2', 'Receptioninst'),
(4,2,'2020-01-01','2020-01-05', 'Customer3', 'Receptioninst'),
(5,2,'2020-04-01','2020-04-05', 'Customer4', 'Receptioninst'),
(6,2,'2020-05-01','2020-05-05', 'Customer5', 'Receptioninst'),
(7,2,'2020-06-01','2020-06-05', 'Customer6', 'Receptioninst');
