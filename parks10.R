better_park|>
  ggplot(aes(x=area_name, y=popularity)) +  
  geom_boxplot() + 
  ylab("Popularity") + 
  xlab("National Park") + 
  labs(title="Side-by-side Boxplot of Popularity of Famous National Parks")