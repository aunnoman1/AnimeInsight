USE [master]
GO
/****** Object:  Database [AnimeInsight]    Script Date: 04/05/2024 6:36:11 pm ******/
CREATE DATABASE [AnimeInsight]
 CONTAINMENT = NONE
 ON  PRIMARY 
( NAME = N'AnimeInsight', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\AnimeInsight.mdf' , SIZE = 73728KB , MAXSIZE = UNLIMITED, FILEGROWTH = 65536KB )
 LOG ON 
( NAME = N'AnimeInsight_log', FILENAME = N'C:\Program Files\Microsoft SQL Server\MSSQL16.MSSQLSERVER\MSSQL\DATA\AnimeInsight_log.ldf' , SIZE = 139264KB , MAXSIZE = 2048GB , FILEGROWTH = 65536KB )
 WITH CATALOG_COLLATION = DATABASE_DEFAULT, LEDGER = OFF
GO
ALTER DATABASE [AnimeInsight] SET COMPATIBILITY_LEVEL = 160
GO
IF (1 = FULLTEXTSERVICEPROPERTY('IsFullTextInstalled'))
begin
EXEC [AnimeInsight].[dbo].[sp_fulltext_database] @action = 'enable'
end
GO
ALTER DATABASE [AnimeInsight] SET ANSI_NULL_DEFAULT OFF 
GO
ALTER DATABASE [AnimeInsight] SET ANSI_NULLS OFF 
GO
ALTER DATABASE [AnimeInsight] SET ANSI_PADDING OFF 
GO
ALTER DATABASE [AnimeInsight] SET ANSI_WARNINGS OFF 
GO
ALTER DATABASE [AnimeInsight] SET ARITHABORT OFF 
GO
ALTER DATABASE [AnimeInsight] SET AUTO_CLOSE OFF 
GO
ALTER DATABASE [AnimeInsight] SET AUTO_SHRINK OFF 
GO
ALTER DATABASE [AnimeInsight] SET AUTO_UPDATE_STATISTICS ON 
GO
ALTER DATABASE [AnimeInsight] SET CURSOR_CLOSE_ON_COMMIT OFF 
GO
ALTER DATABASE [AnimeInsight] SET CURSOR_DEFAULT  GLOBAL 
GO
ALTER DATABASE [AnimeInsight] SET CONCAT_NULL_YIELDS_NULL OFF 
GO
ALTER DATABASE [AnimeInsight] SET NUMERIC_ROUNDABORT OFF 
GO
ALTER DATABASE [AnimeInsight] SET QUOTED_IDENTIFIER OFF 
GO
ALTER DATABASE [AnimeInsight] SET RECURSIVE_TRIGGERS OFF 
GO
ALTER DATABASE [AnimeInsight] SET  ENABLE_BROKER 
GO
ALTER DATABASE [AnimeInsight] SET AUTO_UPDATE_STATISTICS_ASYNC OFF 
GO
ALTER DATABASE [AnimeInsight] SET DATE_CORRELATION_OPTIMIZATION OFF 
GO
ALTER DATABASE [AnimeInsight] SET TRUSTWORTHY OFF 
GO
ALTER DATABASE [AnimeInsight] SET ALLOW_SNAPSHOT_ISOLATION OFF 
GO
ALTER DATABASE [AnimeInsight] SET PARAMETERIZATION SIMPLE 
GO
ALTER DATABASE [AnimeInsight] SET READ_COMMITTED_SNAPSHOT OFF 
GO
ALTER DATABASE [AnimeInsight] SET HONOR_BROKER_PRIORITY OFF 
GO
ALTER DATABASE [AnimeInsight] SET RECOVERY FULL 
GO
ALTER DATABASE [AnimeInsight] SET  MULTI_USER 
GO
ALTER DATABASE [AnimeInsight] SET PAGE_VERIFY CHECKSUM  
GO
ALTER DATABASE [AnimeInsight] SET DB_CHAINING OFF 
GO
ALTER DATABASE [AnimeInsight] SET FILESTREAM( NON_TRANSACTED_ACCESS = OFF ) 
GO
ALTER DATABASE [AnimeInsight] SET TARGET_RECOVERY_TIME = 60 SECONDS 
GO
ALTER DATABASE [AnimeInsight] SET DELAYED_DURABILITY = DISABLED 
GO
ALTER DATABASE [AnimeInsight] SET ACCELERATED_DATABASE_RECOVERY = OFF  
GO
EXEC sys.sp_db_vardecimal_storage_format N'AnimeInsight', N'ON'
GO
ALTER DATABASE [AnimeInsight] SET QUERY_STORE = ON
GO
ALTER DATABASE [AnimeInsight] SET QUERY_STORE (OPERATION_MODE = READ_WRITE, CLEANUP_POLICY = (STALE_QUERY_THRESHOLD_DAYS = 30), DATA_FLUSH_INTERVAL_SECONDS = 900, INTERVAL_LENGTH_MINUTES = 60, MAX_STORAGE_SIZE_MB = 1000, QUERY_CAPTURE_MODE = AUTO, SIZE_BASED_CLEANUP_MODE = AUTO, MAX_PLANS_PER_QUERY = 200, WAIT_STATS_CAPTURE_MODE = ON)
GO
USE [AnimeInsight]
GO
/****** Object:  Table [dbo].[Anime_Metadata]    Script Date: 04/05/2024 6:36:11 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[Anime_Metadata](
	[anime_id] [int] NOT NULL,
	[Name] [nvarchar](200) NOT NULL,
	[English_name] [nvarchar](200) NULL,
	[Score] [float] NULL,
	[Genres] [nvarchar](100) NULL,
	[Synopsis] [nvarchar](max) NOT NULL,
	[Type] [nvarchar](50) NULL,
	[Episodes] [smallint] NULL,
	[Aired] [nvarchar](50) NOT NULL,
	[Premiered] [nvarchar](50) NULL,
	[Status] [nvarchar](50) NOT NULL,
	[Producers] [nvarchar](1550) NULL,
	[Licensors] [nvarchar](100) NULL,
	[Studios] [nvarchar](200) NULL,
	[Source] [nvarchar](50) NULL,
	[Duration] [nvarchar](50) NULL,
	[Age_Rating] [nvarchar](50) NULL,
	[Rank] [int] NULL,
	[Scored_By] [int] NULL,
	[Image_URL] [nvarchar](100) NOT NULL,
 CONSTRAINT [PK_anime-dataset-2023] PRIMARY KEY CLUSTERED 
(
	[anime_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[AnimeInsightApp_favgenres]    Script Date: 04/05/2024 6:36:11 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[AnimeInsightApp_favgenres](
	[id] [bigint] IDENTITY(1,1) NOT NULL,
	[genre] [nvarchar](20) NOT NULL,
	[userid_id] [bigint] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[AnimeInsightApp_profile]    Script Date: 04/05/2024 6:36:11 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[AnimeInsightApp_profile](
	[dob] [date] NOT NULL,
	[registered] [bit] NOT NULL,
	[userid_id] [bigint] NOT NULL,
 CONSTRAINT [AnimeInsightApp_profile_userid_id_0e9fd5da_pk] PRIMARY KEY CLUSTERED 
(
	[userid_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[AnimeInsightApp_user]    Script Date: 04/05/2024 6:36:11 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[AnimeInsightApp_user](
	[id] [bigint] IDENTITY(1,1) NOT NULL,
	[password] [nvarchar](128) NOT NULL,
	[last_login] [datetimeoffset](7) NULL,
	[is_superuser] [bit] NOT NULL,
	[username] [nvarchar](150) NOT NULL,
	[first_name] [nvarchar](150) NOT NULL,
	[last_name] [nvarchar](150) NOT NULL,
	[email] [nvarchar](254) NOT NULL,
	[is_staff] [bit] NOT NULL,
	[is_active] [bit] NOT NULL,
	[date_joined] [datetimeoffset](7) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
UNIQUE NONCLUSTERED 
(
	[username] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[AnimeInsightApp_user_groups]    Script Date: 04/05/2024 6:36:11 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[AnimeInsightApp_user_groups](
	[id] [bigint] IDENTITY(1,1) NOT NULL,
	[user_id] [bigint] NOT NULL,
	[group_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[AnimeInsightApp_user_user_permissions]    Script Date: 04/05/2024 6:36:11 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[AnimeInsightApp_user_user_permissions](
	[id] [bigint] IDENTITY(1,1) NOT NULL,
	[user_id] [bigint] NOT NULL,
	[permission_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[auth_group]    Script Date: 04/05/2024 6:36:11 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[auth_group](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](150) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY],
 CONSTRAINT [auth_group_name_a6ea08ec_uniq] UNIQUE NONCLUSTERED 
(
	[name] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[auth_group_permissions]    Script Date: 04/05/2024 6:36:11 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[auth_group_permissions](
	[id] [bigint] IDENTITY(1,1) NOT NULL,
	[group_id] [int] NOT NULL,
	[permission_id] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[auth_permission]    Script Date: 04/05/2024 6:36:11 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[auth_permission](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[name] [nvarchar](255) NOT NULL,
	[content_type_id] [int] NOT NULL,
	[codename] [nvarchar](100) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[django_admin_log]    Script Date: 04/05/2024 6:36:11 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[django_admin_log](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[action_time] [datetimeoffset](7) NOT NULL,
	[object_id] [nvarchar](max) NULL,
	[object_repr] [nvarchar](200) NOT NULL,
	[action_flag] [smallint] NOT NULL,
	[change_message] [nvarchar](max) NOT NULL,
	[content_type_id] [int] NULL,
	[user_id] [bigint] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[django_content_type]    Script Date: 04/05/2024 6:36:11 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[django_content_type](
	[id] [int] IDENTITY(1,1) NOT NULL,
	[app_label] [nvarchar](100) NOT NULL,
	[model] [nvarchar](100) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[django_migrations]    Script Date: 04/05/2024 6:36:11 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[django_migrations](
	[id] [bigint] IDENTITY(1,1) NOT NULL,
	[app] [nvarchar](255) NOT NULL,
	[name] [nvarchar](255) NOT NULL,
	[applied] [datetimeoffset](7) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[django_session]    Script Date: 04/05/2024 6:36:11 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[django_session](
	[session_key] [nvarchar](40) NOT NULL,
	[session_data] [nvarchar](max) NOT NULL,
	[expire_date] [datetimeoffset](7) NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[session_key] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY] TEXTIMAGE_ON [PRIMARY]
GO
/****** Object:  Table [dbo].[historywatch]    Script Date: 04/05/2024 6:36:11 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[historywatch](
	[userID] [bigint] NOT NULL,
	[AnimeID] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[userID] ASC,
	[AnimeID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[rating]    Script Date: 04/05/2024 6:36:11 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[rating](
	[userID] [bigint] NOT NULL,
	[AnimeID] [int] NOT NULL,
	[rating] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[userID] ASC,
	[AnimeID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[recommendation]    Script Date: 04/05/2024 6:36:11 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[recommendation](
	[userID] [bigint] NOT NULL,
	[AnimeID1] [int] NULL,
	[AnimeID2] [int] NULL,
	[AnimeID3] [int] NULL,
	[AnimeID4] [int] NULL,
	[AnimeID5] [int] NULL,
PRIMARY KEY CLUSTERED 
(
	[userID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[request]    Script Date: 04/05/2024 6:36:11 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[request](
	[userID] [bigint] NOT NULL,
	[AnimeName] [varchar](50) NOT NULL
) ON [PRIMARY]
GO
/****** Object:  Table [dbo].[wishlist]    Script Date: 04/05/2024 6:36:11 pm ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
CREATE TABLE [dbo].[wishlist](
	[userID] [bigint] NOT NULL,
	[AnimeID] [int] NOT NULL,
PRIMARY KEY CLUSTERED 
(
	[userID] ASC,
	[AnimeID] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO
/****** Object:  Index [AnimeInsightApp_favgenres_userid_id_ce0498e2]    Script Date: 04/05/2024 6:36:11 pm ******/
CREATE NONCLUSTERED INDEX [AnimeInsightApp_favgenres_userid_id_ce0498e2] ON [dbo].[AnimeInsightApp_favgenres]
(
	[userid_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [AnimeInsightApp_favgenres_userid_id_genre_56a9b3c2_uniq]    Script Date: 04/05/2024 6:36:11 pm ******/
CREATE UNIQUE NONCLUSTERED INDEX [AnimeInsightApp_favgenres_userid_id_genre_56a9b3c2_uniq] ON [dbo].[AnimeInsightApp_favgenres]
(
	[userid_id] ASC,
	[genre] ASC
)
WHERE ([userid_id] IS NOT NULL AND [genre] IS NOT NULL)
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [AnimeInsightApp_user_groups_group_id_d2601de6]    Script Date: 04/05/2024 6:36:11 pm ******/
CREATE NONCLUSTERED INDEX [AnimeInsightApp_user_groups_group_id_d2601de6] ON [dbo].[AnimeInsightApp_user_groups]
(
	[group_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [AnimeInsightApp_user_groups_user_id_52539e94]    Script Date: 04/05/2024 6:36:11 pm ******/
CREATE NONCLUSTERED INDEX [AnimeInsightApp_user_groups_user_id_52539e94] ON [dbo].[AnimeInsightApp_user_groups]
(
	[user_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [AnimeInsightApp_user_groups_user_id_group_id_63df00c7_uniq]    Script Date: 04/05/2024 6:36:12 pm ******/
CREATE UNIQUE NONCLUSTERED INDEX [AnimeInsightApp_user_groups_user_id_group_id_63df00c7_uniq] ON [dbo].[AnimeInsightApp_user_groups]
(
	[user_id] ASC,
	[group_id] ASC
)
WHERE ([user_id] IS NOT NULL AND [group_id] IS NOT NULL)
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [AnimeInsightApp_user_user_permissions_permission_id_a7383b7f]    Script Date: 04/05/2024 6:36:12 pm ******/
CREATE NONCLUSTERED INDEX [AnimeInsightApp_user_user_permissions_permission_id_a7383b7f] ON [dbo].[AnimeInsightApp_user_user_permissions]
(
	[permission_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [AnimeInsightApp_user_user_permissions_user_id_237b9dd4]    Script Date: 04/05/2024 6:36:12 pm ******/
CREATE NONCLUSTERED INDEX [AnimeInsightApp_user_user_permissions_user_id_237b9dd4] ON [dbo].[AnimeInsightApp_user_user_permissions]
(
	[user_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [AnimeInsightApp_user_user_permissions_user_id_permission_id_ec69617e_uniq]    Script Date: 04/05/2024 6:36:12 pm ******/
CREATE UNIQUE NONCLUSTERED INDEX [AnimeInsightApp_user_user_permissions_user_id_permission_id_ec69617e_uniq] ON [dbo].[AnimeInsightApp_user_user_permissions]
(
	[user_id] ASC,
	[permission_id] ASC
)
WHERE ([user_id] IS NOT NULL AND [permission_id] IS NOT NULL)
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [auth_group_permissions_group_id_b120cbf9]    Script Date: 04/05/2024 6:36:12 pm ******/
CREATE NONCLUSTERED INDEX [auth_group_permissions_group_id_b120cbf9] ON [dbo].[auth_group_permissions]
(
	[group_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [auth_group_permissions_group_id_permission_id_0cd325b0_uniq]    Script Date: 04/05/2024 6:36:12 pm ******/
CREATE UNIQUE NONCLUSTERED INDEX [auth_group_permissions_group_id_permission_id_0cd325b0_uniq] ON [dbo].[auth_group_permissions]
(
	[group_id] ASC,
	[permission_id] ASC
)
WHERE ([group_id] IS NOT NULL AND [permission_id] IS NOT NULL)
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [auth_group_permissions_permission_id_84c5c92e]    Script Date: 04/05/2024 6:36:12 pm ******/
CREATE NONCLUSTERED INDEX [auth_group_permissions_permission_id_84c5c92e] ON [dbo].[auth_group_permissions]
(
	[permission_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [auth_permission_content_type_id_2f476e4b]    Script Date: 04/05/2024 6:36:12 pm ******/
CREATE NONCLUSTERED INDEX [auth_permission_content_type_id_2f476e4b] ON [dbo].[auth_permission]
(
	[content_type_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [auth_permission_content_type_id_codename_01ab375a_uniq]    Script Date: 04/05/2024 6:36:12 pm ******/
CREATE UNIQUE NONCLUSTERED INDEX [auth_permission_content_type_id_codename_01ab375a_uniq] ON [dbo].[auth_permission]
(
	[content_type_id] ASC,
	[codename] ASC
)
WHERE ([content_type_id] IS NOT NULL AND [codename] IS NOT NULL)
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [django_admin_log_content_type_id_c4bce8eb]    Script Date: 04/05/2024 6:36:12 pm ******/
CREATE NONCLUSTERED INDEX [django_admin_log_content_type_id_c4bce8eb] ON [dbo].[django_admin_log]
(
	[content_type_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [django_admin_log_user_id_c564eba6]    Script Date: 04/05/2024 6:36:12 pm ******/
CREATE NONCLUSTERED INDEX [django_admin_log_user_id_c564eba6] ON [dbo].[django_admin_log]
(
	[user_id] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
SET ANSI_PADDING ON
GO
/****** Object:  Index [django_content_type_app_label_model_76bd3d3b_uniq]    Script Date: 04/05/2024 6:36:12 pm ******/
CREATE UNIQUE NONCLUSTERED INDEX [django_content_type_app_label_model_76bd3d3b_uniq] ON [dbo].[django_content_type]
(
	[app_label] ASC,
	[model] ASC
)
WHERE ([app_label] IS NOT NULL AND [model] IS NOT NULL)
WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, IGNORE_DUP_KEY = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
/****** Object:  Index [django_session_expire_date_a5c62663]    Script Date: 04/05/2024 6:36:12 pm ******/
CREATE NONCLUSTERED INDEX [django_session_expire_date_a5c62663] ON [dbo].[django_session]
(
	[expire_date] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, SORT_IN_TEMPDB = OFF, DROP_EXISTING = OFF, ONLINE = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
GO
ALTER TABLE [dbo].[AnimeInsightApp_favgenres]  WITH CHECK ADD  CONSTRAINT [AnimeInsightApp_favgenres_userid_id_ce0498e2_fk_AnimeInsightApp_user_id] FOREIGN KEY([userid_id])
REFERENCES [dbo].[AnimeInsightApp_user] ([id])
GO
ALTER TABLE [dbo].[AnimeInsightApp_favgenres] CHECK CONSTRAINT [AnimeInsightApp_favgenres_userid_id_ce0498e2_fk_AnimeInsightApp_user_id]
GO
ALTER TABLE [dbo].[AnimeInsightApp_profile]  WITH CHECK ADD  CONSTRAINT [AnimeInsightApp_profile_userid_id_0e9fd5da_fk_AnimeInsightApp_user_id] FOREIGN KEY([userid_id])
REFERENCES [dbo].[AnimeInsightApp_user] ([id])
GO
ALTER TABLE [dbo].[AnimeInsightApp_profile] CHECK CONSTRAINT [AnimeInsightApp_profile_userid_id_0e9fd5da_fk_AnimeInsightApp_user_id]
GO
ALTER TABLE [dbo].[AnimeInsightApp_user_groups]  WITH CHECK ADD  CONSTRAINT [AnimeInsightApp_user_groups_group_id_d2601de6_fk_auth_group_id] FOREIGN KEY([group_id])
REFERENCES [dbo].[auth_group] ([id])
GO
ALTER TABLE [dbo].[AnimeInsightApp_user_groups] CHECK CONSTRAINT [AnimeInsightApp_user_groups_group_id_d2601de6_fk_auth_group_id]
GO
ALTER TABLE [dbo].[AnimeInsightApp_user_groups]  WITH CHECK ADD  CONSTRAINT [AnimeInsightApp_user_groups_user_id_52539e94_fk_AnimeInsightApp_user_id] FOREIGN KEY([user_id])
REFERENCES [dbo].[AnimeInsightApp_user] ([id])
GO
ALTER TABLE [dbo].[AnimeInsightApp_user_groups] CHECK CONSTRAINT [AnimeInsightApp_user_groups_user_id_52539e94_fk_AnimeInsightApp_user_id]
GO
ALTER TABLE [dbo].[AnimeInsightApp_user_user_permissions]  WITH CHECK ADD  CONSTRAINT [AnimeInsightApp_user_user_permissions_permission_id_a7383b7f_fk_auth_permission_id] FOREIGN KEY([permission_id])
REFERENCES [dbo].[auth_permission] ([id])
GO
ALTER TABLE [dbo].[AnimeInsightApp_user_user_permissions] CHECK CONSTRAINT [AnimeInsightApp_user_user_permissions_permission_id_a7383b7f_fk_auth_permission_id]
GO
ALTER TABLE [dbo].[AnimeInsightApp_user_user_permissions]  WITH CHECK ADD  CONSTRAINT [AnimeInsightApp_user_user_permissions_user_id_237b9dd4_fk_AnimeInsightApp_user_id] FOREIGN KEY([user_id])
REFERENCES [dbo].[AnimeInsightApp_user] ([id])
GO
ALTER TABLE [dbo].[AnimeInsightApp_user_user_permissions] CHECK CONSTRAINT [AnimeInsightApp_user_user_permissions_user_id_237b9dd4_fk_AnimeInsightApp_user_id]
GO
ALTER TABLE [dbo].[auth_group_permissions]  WITH CHECK ADD  CONSTRAINT [auth_group_permissions_group_id_b120cbf9_fk_auth_group_id] FOREIGN KEY([group_id])
REFERENCES [dbo].[auth_group] ([id])
GO
ALTER TABLE [dbo].[auth_group_permissions] CHECK CONSTRAINT [auth_group_permissions_group_id_b120cbf9_fk_auth_group_id]
GO
ALTER TABLE [dbo].[auth_group_permissions]  WITH CHECK ADD  CONSTRAINT [auth_group_permissions_permission_id_84c5c92e_fk_auth_permission_id] FOREIGN KEY([permission_id])
REFERENCES [dbo].[auth_permission] ([id])
GO
ALTER TABLE [dbo].[auth_group_permissions] CHECK CONSTRAINT [auth_group_permissions_permission_id_84c5c92e_fk_auth_permission_id]
GO
ALTER TABLE [dbo].[auth_permission]  WITH CHECK ADD  CONSTRAINT [auth_permission_content_type_id_2f476e4b_fk_django_content_type_id] FOREIGN KEY([content_type_id])
REFERENCES [dbo].[django_content_type] ([id])
GO
ALTER TABLE [dbo].[auth_permission] CHECK CONSTRAINT [auth_permission_content_type_id_2f476e4b_fk_django_content_type_id]
GO
ALTER TABLE [dbo].[django_admin_log]  WITH CHECK ADD  CONSTRAINT [django_admin_log_content_type_id_c4bce8eb_fk_django_content_type_id] FOREIGN KEY([content_type_id])
REFERENCES [dbo].[django_content_type] ([id])
GO
ALTER TABLE [dbo].[django_admin_log] CHECK CONSTRAINT [django_admin_log_content_type_id_c4bce8eb_fk_django_content_type_id]
GO
ALTER TABLE [dbo].[django_admin_log]  WITH CHECK ADD  CONSTRAINT [django_admin_log_user_id_c564eba6_fk_AnimeInsightApp_user_id] FOREIGN KEY([user_id])
REFERENCES [dbo].[AnimeInsightApp_user] ([id])
GO
ALTER TABLE [dbo].[django_admin_log] CHECK CONSTRAINT [django_admin_log_user_id_c564eba6_fk_AnimeInsightApp_user_id]
GO
ALTER TABLE [dbo].[historywatch]  WITH CHECK ADD FOREIGN KEY([AnimeID])
REFERENCES [dbo].[Anime_Metadata] ([anime_id])
GO
ALTER TABLE [dbo].[historywatch]  WITH CHECK ADD FOREIGN KEY([userID])
REFERENCES [dbo].[AnimeInsightApp_user] ([id])
GO
ALTER TABLE [dbo].[rating]  WITH CHECK ADD FOREIGN KEY([AnimeID])
REFERENCES [dbo].[Anime_Metadata] ([anime_id])
GO
ALTER TABLE [dbo].[rating]  WITH CHECK ADD FOREIGN KEY([userID])
REFERENCES [dbo].[AnimeInsightApp_user] ([id])
GO
ALTER TABLE [dbo].[recommendation]  WITH CHECK ADD FOREIGN KEY([AnimeID1])
REFERENCES [dbo].[Anime_Metadata] ([anime_id])
GO
ALTER TABLE [dbo].[recommendation]  WITH CHECK ADD FOREIGN KEY([AnimeID2])
REFERENCES [dbo].[Anime_Metadata] ([anime_id])
GO
ALTER TABLE [dbo].[recommendation]  WITH CHECK ADD FOREIGN KEY([AnimeID3])
REFERENCES [dbo].[Anime_Metadata] ([anime_id])
GO
ALTER TABLE [dbo].[recommendation]  WITH CHECK ADD FOREIGN KEY([AnimeID4])
REFERENCES [dbo].[Anime_Metadata] ([anime_id])
GO
ALTER TABLE [dbo].[recommendation]  WITH CHECK ADD FOREIGN KEY([AnimeID5])
REFERENCES [dbo].[Anime_Metadata] ([anime_id])
GO
ALTER TABLE [dbo].[recommendation]  WITH CHECK ADD FOREIGN KEY([userID])
REFERENCES [dbo].[AnimeInsightApp_user] ([id])
GO
ALTER TABLE [dbo].[request]  WITH CHECK ADD FOREIGN KEY([userID])
REFERENCES [dbo].[AnimeInsightApp_user] ([id])
GO
ALTER TABLE [dbo].[wishlist]  WITH CHECK ADD FOREIGN KEY([AnimeID])
REFERENCES [dbo].[Anime_Metadata] ([anime_id])
GO
ALTER TABLE [dbo].[wishlist]  WITH CHECK ADD FOREIGN KEY([userID])
REFERENCES [dbo].[AnimeInsightApp_user] ([id])
GO
ALTER TABLE [dbo].[django_admin_log]  WITH CHECK ADD  CONSTRAINT [django_admin_log_action_flag_a8637d59_check] CHECK  (([action_flag]>=(0)))
GO
ALTER TABLE [dbo].[django_admin_log] CHECK CONSTRAINT [django_admin_log_action_flag_a8637d59_check]
GO
USE [master]
GO
ALTER DATABASE [AnimeInsight] SET  READ_WRITE 
GO
