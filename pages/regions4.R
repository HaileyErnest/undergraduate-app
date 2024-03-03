enriched_min_wage|>
  filter(Region != "Other", Year > 2009)|>
  ggplot(aes(x=factor(Year), 
             y=Effective.Minimum.Wage.2020.Dollars, 
             color=factor(Region)))+
  geom_boxplot(outlier.shape = NA)+
  labs(x="Year", y="Effective Minimum Wage (in 2020 Dollars)", title="Minimum Wage of US Regions from 2010-2020 Distribution")+ 
  guides(color = guide_legend(title = "Region"))