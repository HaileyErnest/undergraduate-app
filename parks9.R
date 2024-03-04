park_data <- national_park %>%
  filter(area_name %in% c("Yosemite National Park", "Yellowstone National Park"))

better_park <- national_park |>
  filter(area_name %in% c("Yosemite National Park", "Yellowstone National Park"))|>
  select(area_name, avg_rating, popularity)

t_test_rating_result <- t.test(avg_rating ~ area_name, data = better_park)
t_test_popularity_result <- t.test(popularity ~ area_name, data = better_park)

print(t_test_rating_result)
print(t_test_popularity_result)