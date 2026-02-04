from sqlalchemy import create_engine

engine = create_engine(
    "postgresql+psycopg2://postgres.unobzvvcnumgglngjjpb:66aCkyJsQgCoEISG"
    "@aws-1-us-east-1.pooler.supabase.com:5432/postgres"
)

with engine.connect() as conn:
    print("🔥 Conectado correctamente a Supabase")