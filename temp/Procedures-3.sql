





-- T3_DeleteAnime
CREATE PROCEDURE T3_DeleteAnime
    @p_anime_id INT
AS
BEGIN
    DELETE FROM wl_anime
    WHERE anime_id = @p_anime_id;
END
GO

-- T11_GetWishlist
CREATE PROCEDURE T11_GetWishlist
    @p_user_id INT
AS
BEGIN
    SELECT a.*
    FROM wl_anime a
    JOIN wishlist w ON a.anime_id = w.anime_id
    WHERE w.user_id = @p_user_id;
END
GO

-- T10_RemoveAnimeFromWishlist
CREATE PROCEDURE T10_RemoveAnimeFromWishlist
    @p_user_id INT,
    @p_anime_id INT
AS
BEGIN
    DELETE FROM wishlist
    WHERE user_id = @p_user_id
    AND anime_id = @p_anime_id;
END
GO

--  watch histort
CREATE PROCEDURE AddWatchHistory
    @user_id INT,
    @anime_id INT
AS
BEGIN
    INSERT INTO WatchHistory (user_id, anime_id)
    VALUES (@user_id, @anime_id);
END;

-- del 
CREATE PROCEDURE DeleteWatchHistory
    @user_id INT,
    @anime_id INT
AS
BEGIN
    DELETE FROM WatchHistory
    WHERE user_id = @user_id
    AND anime_id = @anime_id;
END;

