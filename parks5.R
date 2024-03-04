recommend_trails <- function(data, park_name, min_elev = 0, max_elev = Inf, min_rating = 0, trl_type = NULL){

  stopifnot(is.data.frame(data),
            is.numeric(min_elev),
            is.numeric(max_elev),
            is.numeric(min_rating))
  
  recommended_trails <- data |>
    filter(area_name == park_name,
           elevation_gain >= min_elev,
           elevation_gain <= max_elev,
           avg_rating >= min_rating)

  if (!missing(trl_type)) {
    recommended_trails <- recommended_trails |>
      filter(route_type %in% trl_type)
  }
  
  recommended_trails <- recommended_trails |>
    select(name)
  
  return(recommended_trails)
}