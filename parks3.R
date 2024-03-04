national_park|>
  filter(str_detect(area_name, "Mount|Mt|Mountain"))|>
  count()