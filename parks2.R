national_park|>
  mutate(length_km = length*0.001)|>
  filter(elevation_gain < 500, difficulty_rating < 4, length_km < 5)|>
  group_by(area_name)|>
  summarise(easy_trail_num = n())|>
  slice_max(n=1, order_by = easy_trail_num)