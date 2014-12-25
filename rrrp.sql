BEGIN;
CREATE TABLE `rrrp_user` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `username` varchar(200) NOT NULL,
    `password` varchar(200) NOT NULL,
    `flag` bool NOT NULL
)
;
CREATE TABLE `rrrp_log` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `user_id` integer NOT NULL,
    `log_info` longtext NOT NULL
)
;
ALTER TABLE `rrrp_log` ADD CONSTRAINT `user_id_refs_id_3d666cd4` FOREIGN KEY (`user_id`) REFERENCES `rrrp_user` (`id`);
CREATE INDEX `rrrp_log_6340c63c` ON `rrrp_log` (`user_id`);

CREATE TABLE `auth_permission` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(50) NOT NULL,
    `content_type_id` integer NOT NULL,
    `codename` varchar(100) NOT NULL,
    UNIQUE (`content_type_id` , `codename`)
)
;
ALTER TABLE `auth_permission` ADD CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
CREATE TABLE `auth_group_permissions` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `group_id` integer NOT NULL,
    `permission_id` integer NOT NULL,
    UNIQUE (`group_id` , `permission_id`)
)
;
ALTER TABLE `auth_group_permissions` ADD CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
CREATE TABLE `auth_group` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(80) NOT NULL UNIQUE
)
;
ALTER TABLE `auth_group_permissions` ADD CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);
CREATE TABLE `auth_user_groups` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `user_id` integer NOT NULL,
    `group_id` integer NOT NULL,
    UNIQUE (`user_id` , `group_id`)
)
;
ALTER TABLE `auth_user_groups` ADD CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);
CREATE TABLE `auth_user_user_permissions` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `user_id` integer NOT NULL,
    `permission_id` integer NOT NULL,
    UNIQUE (`user_id` , `permission_id`)
)
;
ALTER TABLE `auth_user_user_permissions` ADD CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
CREATE TABLE `auth_user` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `password` varchar(128) NOT NULL,
    `last_login` datetime NOT NULL,
    `is_superuser` bool NOT NULL,
    `username` varchar(30) NOT NULL UNIQUE,
    `first_name` varchar(30) NOT NULL,
    `last_name` varchar(30) NOT NULL,
    `email` varchar(75) NOT NULL,
    `is_staff` bool NOT NULL,
    `is_active` bool NOT NULL,
    `date_joined` datetime NOT NULL
)
;
ALTER TABLE `auth_user_groups` ADD CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `auth_user_user_permissions` ADD CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
CREATE INDEX `auth_permission_37ef4eb4` ON `auth_permission` (`content_type_id`);

CREATE TABLE `django_content_type` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(100) NOT NULL,
    `app_label` varchar(100) NOT NULL,
    `model` varchar(100) NOT NULL,
    UNIQUE (`app_label` , `model`)
)
;
CREATE TABLE `django_session` (
    `session_key` varchar(40) NOT NULL PRIMARY KEY,
    `session_data` longtext NOT NULL,
    `expire_date` datetime NOT NULL
)
;
CREATE INDEX `django_session_b7b81f0c` ON `django_session` (`expire_date`);

CREATE TABLE `django_site` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `domain` varchar(100) NOT NULL,
    `name` varchar(50) NOT NULL
)
;