from analytics import Research
from config import num_of_steps, report_template
import sys
res=Research(sys.argv[1])
data = res.file_reader()
observations = len(data)
analitics=res.Analytics(data) 
heads, tails = analitics.counts(data)
heads_percent, tails_percent = analitics.fractions()
predicted_heads,predicted_tails = analitics.counts(analitics.predict_random(num_of_steps))
report=report_template.format(
    observations=observations,
    tails=tails,
    heads=heads,
    tails_percent=tails_percent,
    heads_percent=heads_percent,
    num_of_steps=num_of_steps,
    predicted_tails=predicted_tails,
    predicted_heads=predicted_heads
)
analitics.save_file(report,"report","txt")