enriched_min_wage |>
  filter(1980>Year)|>
  group_by(Region)|>
  summarise(
    mean_effective_wage = mean(Effective.Minimum.Wage.2020.Dollars),
    var_effective_wage = var(Effective.Minimum.Wage.2020.Dollars))|>
  slice_max(var_effective_wage, n=5)