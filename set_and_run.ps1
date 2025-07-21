# set_and_run.ps1
$env:PINECONE_API_KEY='pcsk_3e6iuw_TEoyF1A4ESKpGFp8ZJ7FXg7EQF6p5yxYxK6y7kdKN26KGTJY5NGX3dEgg3uaio'
$env:PINECONE_ENVIRONMENT='YOUR_ENVIRONMENT_HERE' # e.g., 'gcp-starter' or 'us-west-2'

# Verify (optional)
Write-Host "PINECONE_API_KEY is: $($env:PINECONE_API_KEY)"
Write-Host "PINECONE_ENVIRONMENT is: $($env:PINECONE_ENVIRONMENT)"

# Now run your Streamlit app
streamlit run semantic_search.py