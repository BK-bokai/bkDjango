-- phpMyAdmin SQL Dump
-- version 4.9.0.1
-- https://www.phpmyadmin.net/
--
-- 主機： 127.0.0.1
-- 產生時間： 2019-11-29 10:53:49
-- 伺服器版本： 10.3.16-MariaDB
-- PHP 版本： 7.3.7

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 資料庫： `bkdjango`
--

-- --------------------------------------------------------

--
-- 資料表結構 `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add question', 7, 'add_question'),
(26, 'Can change question', 7, 'change_question'),
(27, 'Can delete question', 7, 'delete_question'),
(28, 'Can view question', 7, 'view_question'),
(29, 'Can add choice', 8, 'add_choice'),
(30, 'Can change choice', 8, 'change_choice'),
(31, 'Can delete choice', 8, 'delete_choice'),
(32, 'Can view choice', 8, 'view_choice'),
(33, 'Can add food', 9, 'add_food'),
(34, 'Can change food', 9, 'change_food'),
(35, 'Can delete food', 9, 'delete_food'),
(36, 'Can view food', 9, 'view_food'),
(37, 'Can add restaurant', 10, 'add_restaurant'),
(38, 'Can change restaurant', 10, 'change_restaurant'),
(39, 'Can delete restaurant', 10, 'delete_restaurant'),
(40, 'Can view restaurant', 10, 'view_restaurant'),
(41, 'Can add author', 11, 'add_author'),
(42, 'Can change author', 11, 'change_author'),
(43, 'Can delete author', 11, 'delete_author'),
(44, 'Can view author', 11, 'view_author'),
(45, 'Can add book', 12, 'add_book'),
(46, 'Can change book', 12, 'change_book'),
(47, 'Can delete book', 12, 'delete_book'),
(48, 'Can view book', 12, 'view_book'),
(49, 'Can add comment', 13, 'add_comment'),
(50, 'Can change comment', 13, 'change_comment'),
(51, 'Can delete comment', 13, 'delete_comment'),
(52, 'Can view comment', 13, 'view_comment');

-- --------------------------------------------------------

--
-- 資料表結構 `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$150000$gyKcXtcSonko$b5PLXqnp/UX6XJrAEyi4NH9VRf3NxrTmpRYEXrY+NWg=', '2019-11-26 02:42:39.176405', 1, 'bokai', '', '', 'bokai830124@gmail.com', 1, 1, '2019-11-26 02:41:58.442106');

-- --------------------------------------------------------

--
-- 資料表結構 `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 資料表結構 `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext DEFAULT NULL,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2019-11-26 03:05:18.077782', '4', 'test', 1, '[{\"added\": {}}]', 7, 1);

-- --------------------------------------------------------

--
-- 資料表結構 `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(8, 'polls', 'choice'),
(7, 'polls', 'question'),
(11, 'restaurants', 'author'),
(12, 'restaurants', 'book'),
(13, 'restaurants', 'comment'),
(9, 'restaurants', 'food'),
(10, 'restaurants', 'restaurant'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- 資料表結構 `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-11-22 09:27:30.531356'),
(2, 'auth', '0001_initial', '2019-11-22 09:27:30.646363'),
(3, 'admin', '0001_initial', '2019-11-22 09:27:31.044385'),
(4, 'admin', '0002_logentry_remove_auto_add', '2019-11-22 09:27:31.092388'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2019-11-22 09:27:31.111389'),
(6, 'contenttypes', '0002_remove_content_type_name', '2019-11-22 09:27:31.184393'),
(7, 'auth', '0002_alter_permission_name_max_length', '2019-11-22 09:27:31.207395'),
(8, 'auth', '0003_alter_user_email_max_length', '2019-11-22 09:27:31.259398'),
(9, 'auth', '0004_alter_user_username_opts', '2019-11-22 09:27:31.267398'),
(10, 'auth', '0005_alter_user_last_login_null', '2019-11-22 09:27:31.290399'),
(11, 'auth', '0006_require_contenttypes_0002', '2019-11-22 09:27:31.291400'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2019-11-22 09:27:31.301400'),
(13, 'auth', '0008_alter_user_username_max_length', '2019-11-22 09:27:31.326402'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2019-11-22 09:27:31.375404'),
(15, 'auth', '0010_alter_group_name_max_length', '2019-11-22 09:27:31.404406'),
(16, 'auth', '0011_update_proxy_permissions', '2019-11-22 09:27:31.413406'),
(17, 'sessions', '0001_initial', '2019-11-22 09:27:31.424407'),
(18, 'polls', '0001_initial', '2019-11-26 01:46:33.173723'),
(19, 'polls', '0002_auto_20191126_1014', '2019-11-26 02:53:33.172965'),
(20, 'polls', '0003_auto_20191126_1052', '2019-11-26 02:53:33.278971'),
(21, 'polls', '0004_question_modify_date', '2019-11-26 02:54:11.879025'),
(22, 'polls', '0005_auto_20191126_1754', '2019-11-26 09:55:01.983806'),
(23, 'restaurants', '0001_initial', '2019-11-27 09:32:31.651400'),
(24, 'restaurants', '0002_auto_20191128_1405', '2019-11-28 06:21:09.824110'),
(25, 'restaurants', '0003_author_book', '2019-11-28 06:21:09.926116'),
(26, 'restaurants', '0004_restaurant_comment', '2019-11-29 03:05:06.986281'),
(27, 'restaurants', '0005_remove_restaurant_comment', '2019-11-29 03:06:54.936100'),
(28, 'restaurants', '0006_comment', '2019-11-29 03:10:15.755173');

-- --------------------------------------------------------

--
-- 資料表結構 `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('dj1ez63ly0jdaqh550o2l125cac0rkne', 'YmEyMDMwM2NkOTJlZDc2NTdmOGE3ODM0ODZlMTAyYzAwZjNhZmZhNTp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI0ZjI5ODhhMjRjM2Q0NjJiNWRhYmY5ZWFkYTA0NTFmY2Y4NGY0MjFiIn0=', '2019-12-10 02:42:39.179405');

-- --------------------------------------------------------

--
-- 資料表結構 `polls_choice`
--

CREATE TABLE `polls_choice` (
  `id` int(11) NOT NULL,
  `choice_text` varchar(200) NOT NULL,
  `votes` int(11) NOT NULL,
  `question_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `polls_choice`
--

INSERT INTO `polls_choice` (`id`, `choice_text`, `votes`, `question_id`) VALUES
(4, 'much none', 3, 2),
(5, 'good', 7, 2),
(6, 'bad', 2, 2);

-- --------------------------------------------------------

--
-- 資料表結構 `polls_question`
--

CREATE TABLE `polls_question` (
  `id` int(11) NOT NULL,
  `question_text` varchar(200) NOT NULL,
  `pub_date` datetime(6) NOT NULL,
  `modify_date` datetime(6) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `polls_question`
--

INSERT INTO `polls_question` (`id`, `question_text`, `pub_date`, `modify_date`) VALUES
(2, 'what is now', '2019-11-26 02:47:06.602460', NULL),
(3, 'What is your name', '2019-11-26 02:56:53.163684', NULL),
(4, 'test', '2019-11-26 03:05:18.054781', '2019-11-26 03:05:00.000000'),
(5, 'test2', '2019-11-26 03:11:07.953272', NULL),
(6, 'test4', '2019-11-26 11:19:37.291586', NULL);

-- --------------------------------------------------------

--
-- 資料表結構 `restaurants_author`
--

CREATE TABLE `restaurants_author` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `restaurants_author`
--

INSERT INTO `restaurants_author` (`id`, `name`) VALUES
(1, '金庸'),
(2, '古龍'),
(3, '李白'),
(4, '白居易');

-- --------------------------------------------------------

--
-- 資料表結構 `restaurants_book`
--

CREATE TABLE `restaurants_book` (
  `id` int(11) NOT NULL,
  `title` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `restaurants_book`
--

INSERT INTO `restaurants_book` (`id`, `title`) VALUES
(1, '唐詩三百首');

-- --------------------------------------------------------

--
-- 資料表結構 `restaurants_book_authors`
--

CREATE TABLE `restaurants_book_authors` (
  `id` int(11) NOT NULL,
  `book_id` int(11) NOT NULL,
  `author_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `restaurants_book_authors`
--

INSERT INTO `restaurants_book_authors` (`id`, `book_id`, `author_id`) VALUES
(1, 1, 3);

-- --------------------------------------------------------

--
-- 資料表結構 `restaurants_comment`
--

CREATE TABLE `restaurants_comment` (
  `id` int(11) NOT NULL,
  `visitor` varchar(20) NOT NULL,
  `content` varchar(200) NOT NULL,
  `email` varchar(200) NOT NULL,
  `publish_date` datetime(6) NOT NULL,
  `Restaurant_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `restaurants_comment`
--

INSERT INTO `restaurants_comment` (`id`, `visitor`, `content`, `email`, `publish_date`, `Restaurant_id`) VALUES
(1, 'Aaron', 'very good', 'test@email.com', '2019-11-29 03:20:28.606176', 1),
(2, 'test', 'test', 'test', '2019-11-29 03:59:33.680450', 1),
(8, 'test', 'qweqw', 'test@', '2019-11-29 05:50:26.710338', 1),
(12, 'ass', 'wdq', 'wdw@we.', '2019-11-29 06:57:21.396801', 1);

-- --------------------------------------------------------

--
-- 資料表結構 `restaurants_food`
--

CREATE TABLE `restaurants_food` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `price` decimal(3,0) NOT NULL,
  `comment` varchar(50) NOT NULL,
  `is_spicy` tinyint(1) NOT NULL,
  `restaurant_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `restaurants_food`
--

INSERT INTO `restaurants_food` (`id`, `name`, `price`, `comment`, `is_spicy`, `restaurant_id`) VALUES
(1, 'apple', '13', 'good', 0, 1),
(2, 'cherry', '10', 'good', 0, 2),
(3, 'patch', '14', 'good', 0, 1),
(4, 'tomato', '9', 'good', 0, 2);

-- --------------------------------------------------------

--
-- 資料表結構 `restaurants_restaurant`
--

CREATE TABLE `restaurants_restaurant` (
  `id` int(11) NOT NULL,
  `name` varchar(20) NOT NULL,
  `phone_number` varchar(15) NOT NULL,
  `address` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 傾印資料表的資料 `restaurants_restaurant`
--

INSERT INTO `restaurants_restaurant` (`id`, `name`, `phone_number`, `address`) VALUES
(1, '蘆洲熱炒', '0923666555', '火星路2段2號'),
(2, '三重海產', '0956958956', '天南路5段2號');

--
-- 已傾印資料表的索引
--

--
-- 資料表索引 `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- 資料表索引 `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- 資料表索引 `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- 資料表索引 `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- 資料表索引 `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- 資料表索引 `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- 資料表索引 `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- 資料表索引 `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- 資料表索引 `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- 資料表索引 `polls_choice`
--
ALTER TABLE `polls_choice`
  ADD PRIMARY KEY (`id`),
  ADD KEY `polls_choice_question_id_c5b4b260_fk_polls_question_id` (`question_id`);

--
-- 資料表索引 `polls_question`
--
ALTER TABLE `polls_question`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `restaurants_author`
--
ALTER TABLE `restaurants_author`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `restaurants_book`
--
ALTER TABLE `restaurants_book`
  ADD PRIMARY KEY (`id`);

--
-- 資料表索引 `restaurants_book_authors`
--
ALTER TABLE `restaurants_book_authors`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `restaurants_book_authors_book_id_author_id_150dd833_uniq` (`book_id`,`author_id`),
  ADD KEY `restaurants_book_aut_author_id_d5b462a6_fk_restauran` (`author_id`);

--
-- 資料表索引 `restaurants_comment`
--
ALTER TABLE `restaurants_comment`
  ADD PRIMARY KEY (`id`),
  ADD KEY `restaurants_comment_Restaurant_id_6059d087_fk_restauran` (`Restaurant_id`);

--
-- 資料表索引 `restaurants_food`
--
ALTER TABLE `restaurants_food`
  ADD PRIMARY KEY (`id`),
  ADD KEY `restaurants_food_restaurant_id_281987c9_fk_restauran` (`restaurant_id`);

--
-- 資料表索引 `restaurants_restaurant`
--
ALTER TABLE `restaurants_restaurant`
  ADD PRIMARY KEY (`id`);

--
-- 在傾印的資料表使用自動遞增(AUTO_INCREMENT)
--

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=53;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `polls_choice`
--
ALTER TABLE `polls_choice`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `polls_question`
--
ALTER TABLE `polls_question`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `restaurants_author`
--
ALTER TABLE `restaurants_author`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `restaurants_book`
--
ALTER TABLE `restaurants_book`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `restaurants_book_authors`
--
ALTER TABLE `restaurants_book_authors`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `restaurants_comment`
--
ALTER TABLE `restaurants_comment`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `restaurants_food`
--
ALTER TABLE `restaurants_food`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- 使用資料表自動遞增(AUTO_INCREMENT) `restaurants_restaurant`
--
ALTER TABLE `restaurants_restaurant`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- 已傾印資料表的限制式
--

--
-- 資料表的限制式 `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- 資料表的限制式 `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- 資料表的限制式 `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 資料表的限制式 `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 資料表的限制式 `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 資料表的限制式 `polls_choice`
--
ALTER TABLE `polls_choice`
  ADD CONSTRAINT `polls_choice_question_id_c5b4b260_fk_polls_question_id` FOREIGN KEY (`question_id`) REFERENCES `polls_question` (`id`);

--
-- 資料表的限制式 `restaurants_book_authors`
--
ALTER TABLE `restaurants_book_authors`
  ADD CONSTRAINT `restaurants_book_aut_author_id_d5b462a6_fk_restauran` FOREIGN KEY (`author_id`) REFERENCES `restaurants_author` (`id`),
  ADD CONSTRAINT `restaurants_book_authors_book_id_ca9c78eb_fk_restaurants_book_id` FOREIGN KEY (`book_id`) REFERENCES `restaurants_book` (`id`);

--
-- 資料表的限制式 `restaurants_comment`
--
ALTER TABLE `restaurants_comment`
  ADD CONSTRAINT `restaurants_comment_Restaurant_id_6059d087_fk_restauran` FOREIGN KEY (`Restaurant_id`) REFERENCES `restaurants_restaurant` (`id`);

--
-- 資料表的限制式 `restaurants_food`
--
ALTER TABLE `restaurants_food`
  ADD CONSTRAINT `restaurants_food_restaurant_id_281987c9_fk_restauran` FOREIGN KEY (`restaurant_id`) REFERENCES `restaurants_restaurant` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
