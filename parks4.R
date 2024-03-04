np_trails_new <- national_park |>
  pivot_longer(
    cols = c(avg_rating, difficulty_rating, popularity, visitor_usage),
    names_to = "measure",
    values_to = "score")

np_trails_new %>%
  ggplot(aes(x=score)) +
  geom_density() +
  facet_wrap(~ measure, scales = 'free') +
  ggtitle("Overall distribution of various trail scores in National parks")