import streamlit as st

# Set page title
st.set_page_config(page_title="Data Warehousing & EDM", layout="wide")

# Sidebar setup
st.sidebar.title("📚 Data Warehousing Topics")
topic = st.sidebar.radio("Choose a topic:", [
    "Overview",
    "ETL Process",
    "Data Integration",
    "Data Governance",
    "Performance Optimization",
    "Big Data & NoSQL",
    "Data Modeling",
])

st.sidebar.markdown("🧠 **Tip:** Explore each section to build a solid understanding of data management in enterprises.")

# Expander for introduction
with st.expander("📖 Introduction: What is Data Warehousing and Enterprise Data Management?"):
    st.write("""
        **Data Warehousing** involves collecting, storing, and managing data from various sources to support business intelligence and decision-making.
        
        **Enterprise Data Management (EDM)** ensures that organizational data is secure, accurate, and available to the right users at the right time.
    """)

# Content rendering based on topic
if topic == "Overview":
    st.header("📦 Overview of Data Warehousing")
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("What is a Data Warehouse?")
        st.write("""
            A Data Warehouse is a central repository for integrated data from multiple sources, optimized for reporting and analysis.
        """)
    with col2:
        st.subheader("Key Components")
        st.markdown("""
        - 🧩 **Data Sources** – Internal/external systems (e.g., CRM, ERP)  
        - 🔄 **ETL Tools** – Extract, Transform, Load pipelines  
        - 🏪 **Data Marts** – Department-specific subsets  
        """)

elif topic == "ETL Process":
    st.header("🔄 ETL Process")
    st.write("""
        The **ETL Process** (Extract, Transform, Load) is foundational for populating a data warehouse:
        
        - **Extract**: Gather raw data from multiple sources  
        - **Transform**: Clean, normalize, and enrich the data  
        - **Load**: Store the transformed data into the data warehouse  
    """)

elif topic == "Data Integration":
    st.header("🔗 Data Integration")
    st.write("""
        Integration combines data from different sources into a unified view:
        
        - **Replication**: Copying data regularly  
        - **Federation**: Querying across sources without physical movement  
        - **Virtualization**: Real-time access to distributed systems  
    """)

elif topic == "Data Governance":
    st.header("🛡️ Data Governance")
    st.write("""
        Data Governance ensures responsible management of data:
        
        - **Data Quality**: Accuracy and completeness  
        - **Data Security**: Protecting sensitive info  
        - **Data Compliance**: GDPR, HIPAA, etc.  
    """)

elif topic == "Performance Optimization":
    st.header("⚡ Performance Optimization")
    st.write("""
        Improve warehouse performance using:
        
        - **Indexing**: Faster query access  
        - **Partitioning**: Manage massive tables  
        - **Query Optimization**: Efficient SQL + caching  
    """)

elif topic == "Big Data & NoSQL":
    st.header("🌍 Big Data & NoSQL")
    st.write("""
        Modern data environments often need to handle vast amounts of data that require NoSQL solutions and Big Data technologies:
        
        - **Big Data**: Tools like Hadoop, Spark, and Flink handle large-scale data processing  
        - **NoSQL Databases**: MongoDB, Cassandra, and others provide flexible schema for unstructured data  
    """)

elif topic == "Data Modeling":
    st.header("📊 Data Modeling")
    st.write("""
        Data modeling helps in structuring data for analysis and storage:
        
        - **Star Schema**: Central fact table surrounded by dimension tables  
        - **Snowflake Schema**: A normalized form of the star schema  
        - **Dimensional Modeling**: Focus on business processes rather than the physical storage  
    """)

# Tabs for extended content
tab1, tab2, tab3 = st.tabs(["📈 Real-Time Analytics", "☁️ Cloud Warehousing", "🗄️ Data Archiving"])

with tab1:
    st.subheader("Real-Time Analytics")
    st.write("Enable instant insights using tools like Apache Kafka, Spark Streaming, and change data capture (CDC) mechanisms.")

with tab2:
    st.subheader("Cloud Data Warehousing")
    st.write("Modern cloud platforms like Snowflake, BigQuery, and Redshift offer scalability, flexibility, and cost-efficiency.")

with tab3:
    st.subheader("Data Archiving")
    st.write("Archiving strategies include cold storage, lifecycle policies, and compliance-driven retention techniques.")

# Additional Sidebar Actions
st.sidebar.subheader("🔧 Data Warehouse Setup Checklist")
st.sidebar.markdown("""
- [ ] Define data sources
- [ ] Choose ETL tools
- [ ] Design data model
- [ ] Select storage solution (cloud/on-premise)
- [ ] Establish security and governance protocols
""")

st.sidebar.subheader("💡 Get More Resources")
st.sidebar.markdown("""
- **Books**: "The Data Warehouse Toolkit" by Ralph Kimball  
- **Tools**: Apache Hadoop, Snowflake, Amazon Redshift  
- **Courses**: Coursera, Udemy, DataCamp  
""")

# Displaying Footer with further info
st.markdown("""
    ---  
    📞 For questions or inquiries, contact us at [support@datacenter.com](mailto:support@datacenter.com)
""")
