# If the cell `shap_values = explainer.shap_values(X_enc_df)` takes too much time to run, please try either:
# - Clone the repository of this project by navigating to Terminal and call `git clone https://github.com/jh22d/BookedUp.git`. Get back to this file and uncomment & run the 3 code cells below.

# or

# - Go to [the repository of this project](https://github.com/jh22d/BookedUp), navigate to the `results/` folder and check the force plots manually.

# And comment out the 3 code cells below that generate the force plots containing the function `shap.force_plot`.

from IPython.display import Image
Image("results/fp1.png")
Image("results/fp2.png")
Image("results/fp3.png")