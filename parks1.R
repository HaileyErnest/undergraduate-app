national_park|>
  filter(state_name == "California")|>
  mutate(length_mi = length*0.000621371) |>
  slice_max(n = 4, order_by = length_mi)|>
  slice(4)|>
  select(name, length_mi)