```
df = df.filter(df.children >= 0)
df = df.withColumn('has_booking_changes', df.booking_changes > 0)
```
