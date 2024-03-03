enriched_min_wage|>
  filter(Region != "Other")|>
  group_by(Region, Year)|>
  summarise(mean_effective_wage = mean(Effective.Minimum.Wage.2020.Dollars))|>
  ggplot(aes(x=Year, y=mean_effective_wage, color=Region))+
  geom_line()+
  labs(x="Year", y="Mean Minimum Wage", title="Average Minimum Wage of US Regions from 1968-2020")