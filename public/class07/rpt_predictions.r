# rpt_predictions.r

# This script should read predictions.csv and report 
# -Long-Only Effectiveness
# -Model Effectiveness
# -Long-Only Accuracy
# -Model Accuracy

# Demo:
# R -f rpt_predictions.r

# I should read predictions.csv
predictions_df = read.csv('predictions.csv')

# I should report Long-Only Effectiveness:
long_only_eff_f = sum(predictions_df$pctlead)
print('long_only_eff:')
print(long_only_eff_f)

# I should calculate Model Effectiveness.
# Logic should be:
# If prediction has same sign as pctlead, that prediction is effective:
predictions_df$effectiveness = sign(predictions_df$prediction) * predictions_df$pctlead

# I should report Model Effectiveness:
model_eff_f = sum(predictions_df$effectiveness)
print('model_eff:')
print(model_eff_f)

# I should calculate Long-Only Accuracy.
pctlead_up_v = sign(predictions_df$pctlead)
# I should count the 1 values
lo_count_up_i = sum(pctlead_up_v == 1)
# Accuracy should be count of up days divided by all days:
lo_accuracy_f = 100.0 * lo_count_up_i / length(predictions_df$pctlead)
print('Long-Only accuracy:')
print(lo_accuracy_f)

# I should calculate model Accuracy.
# If the signs match, that should be accurate:
predictions_df$accuracy = sign(predictions_df$prediction) * sign(predictions_df$pctlead)

# I should count the 1 values
tf_v = (predictions_df$accuracy == 1)
# I should use sum() to sum the 1 values which should be same as count of TRUE values.
true_count_i = sum(tf_v)
all_count_i  = length(predictions_df$accuracy)
accuracy_f   = 100.0 * true_count_i / all_count_i
print('model accuracy:')
print(accuracy_f)

'bye'
