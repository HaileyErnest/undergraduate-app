#Code to add regional groups
region_list <- min_wage |>
  distinct(State)
write.csv(region_list, "./region_list.csv")

#Code to add new Region variable to data frame
enriched_region_list <- read_csv("region_list1.txt", show_col_types = FALSE)

#Code to merge data sets
enriched_min_wage <- full_join(min_wage,enriched_region_list)