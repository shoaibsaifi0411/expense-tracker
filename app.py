import streamlit as st
import expense_manager as em

st.title("personal Expense Manager")

menu = st.sidebar.selectbox(
    "Menu",
    ["Add Expense", "View Expenses", "Total Expenses", "Category-wise Expenses"])

# add expense

if menu == "Add Expense":
    st.subheader("Add Expense")

    date = st.date_input("Date")
    category = st.selectbox("Category", ["Food", "Travel", "Shopping", "Bills", "Other"])
    amount = st.number_input("Amount")

    note = st.text_area("Note")

    if st.button("Add Expense"):
        em.add_expense(str(date), category, amount, note)
        st.success("Expense added successfully!")

 # view expenses
elif menu == "View Expenses":
    st.header("all Expenses")
    expenses = em.get_expenses()
    for e in expenses:
        st.write(
            e["date"], e["category"], e["amount"], e["note"]
        )

# total expenses
elif menu == "Total Expenses":
    st.header("Total spending")
    total = em.total_expenses()
    st.subheader("total expenses = rupees " + str(total))


# category wise expenses
elif menu == "Category-wise Expenses":
    st.header("Category-wise Expenses")
    data = em.category_expenses()
    for cat in data:
        st.write(cat, ": rupees ", data[cat])
