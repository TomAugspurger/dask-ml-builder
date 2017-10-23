function run_tests {
    python --version
    python -c "import dask_ml.utils; dask_ml.utils.test()" 
}
