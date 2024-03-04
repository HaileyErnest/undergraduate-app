national_park |>
  filter(area_name %in% c("Yosemite National Park", "Yellowstone National Park"),
         avg_rating > 3, 
         !str_detect(features, "'dogs-no'"))|>
  ggplot(aes(x=popularity, y=length, color=area_name))+
  geom_line()+
  labs(x = "Popularity", 
       y= "Length (meters)", 
       title = "Popularity of Famous Trails By Trail Length", 
       color="National Park")+
  scale_color_manual(values = c("Yosemite National Park" = "brown", "Yellowstone National Park" = "#CD9600"))