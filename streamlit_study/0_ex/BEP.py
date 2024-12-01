import streamlit as st
import plotly.graph_objects as go
import numpy as np

def format_currency(value):
    """Format number with thousand separator"""
    return f"{value:,.2f}"

def calculate_bep_plotly(revenue_per_unit, variable_cost_per_unit, fixed_costs):
    # Calculate contribution margin
    contribution_margin = revenue_per_unit - variable_cost_per_unit
    contribution_margin_ratio = (contribution_margin / revenue_per_unit) * 100

    # Calculate BEP
    bep_sales = fixed_costs / (contribution_margin / revenue_per_unit)
    bep_units = bep_sales / revenue_per_unit

    # Set sales levels (up to 2x BEP)
    sales = np.linspace(0, 2 * bep_sales, 100)
    units = sales / revenue_per_unit

    # Calculate costs and profit
    total_cost = fixed_costs + (sales * (variable_cost_per_unit / revenue_per_unit))
    revenue = sales
    profit = revenue - total_cost

    # Create Plotly graph
    fig = go.Figure()

    # Revenue line
    fig.add_trace(go.Scatter(
        x=units, y=revenue,
        mode='lines', name='Revenue',
        line=dict(color='#2E86C1', width=3)
    ))

    # Total cost line
    fig.add_trace(go.Scatter(
        x=units, y=total_cost,
        mode='lines', name='Total Cost',
        line=dict(color='#E74C3C', width=3)
    ))

    # Loss area (before BEP)
    loss_x = units[units <= bep_units]
    loss_revenue = revenue[units <= bep_units]
    loss_cost = total_cost[units <= bep_units]

    fig.add_trace(go.Scatter(
        x=list(loss_x) + list(loss_x)[::-1],
        y=list(loss_revenue) + list(loss_cost)[::-1],
        fill='toself',
        fillcolor='rgba(231, 76, 60, 0.2)',
        line=dict(color='rgba(255,255,255,0)'),
        name='Loss Area',
        showlegend=True,
        hoverinfo='skip'
    ))

    # Profit area (after BEP)
    profit_x = units[units > bep_units]
    profit_revenue = revenue[units > bep_units]
    profit_cost = total_cost[units > bep_units]

    fig.add_trace(go.Scatter(
        x=list(profit_x) + list(profit_x)[::-1],
        y=list(profit_revenue) + list(profit_cost)[::-1],
        fill='toself',
        fillcolor='rgba(39, 174, 96, 0.2)',
        line=dict(color='rgba(255,255,255,0)'),
        name='Profit Area',
        showlegend=True,
        hoverinfo='skip'
    ))

    # Fixed cost line
    fig.add_trace(go.Scatter(
        x=units,
        y=[fixed_costs] * len(units),
        mode='lines',
        name='Fixed Cost',
        line=dict(color='#95A5A6', width=2, dash='dash')
    ))

    # Break-even point line
    fig.add_vline(
        x=bep_units,
        line=dict(color='red', dash='dot', width=2),
        annotation_text=f"Break-even Point: {int(bep_units):,} units",
        annotation_position="top"
    )

    # Layout configuration
    fig.update_layout(
        title={
            'text': "Break-Even Point (BEP) Analysis",
            'y': 0.95,
            'x': 0.5,
            'xanchor': 'center',
            'yanchor': 'top',
            'font': dict(size=24)
        },
        xaxis_title="Number of Units",
        yaxis_title="Amount ($)",
        height=700,
        template='plotly_white',
        showlegend=True,
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bgcolor='rgba(0, 0, 0, 0.5)',
            bordercolor='rgba(255, 255, 255, 0.5)',
            borderwidth=1
        )
    )

    # Hover information
    fig.update_traces(
        hovertemplate='Units: %{x:,.0f}<br>Amount: $%{y:,.2f}<extra></extra>'
    )

    # Axis formatting
    fig.update_yaxes(tickformat="$,.2f", gridcolor='rgba(255, 255, 255, 0.1)')
    fig.update_xaxes(showgrid=True, gridwidth=1, gridcolor='rgba(255, 255, 255, 0.1)')
    fig.update_yaxes(showgrid=True, gridwidth=1, gridcolor='rgba(255, 255, 255, 0.1)')

    return fig, {
        'bep_sales': bep_sales,
        'bep_units': bep_units,
        'contribution_margin': contribution_margin,
        'contribution_margin_ratio': contribution_margin_ratio
    }

# Setup page
st.set_page_config(
    page_title="Break-Even Point Analysis",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Break-Even Point Analysis Tool")

st.markdown("""
This tool helps you analyze your break-even point by calculating when your revenue equals your total costs.
Enter your financial data below to generate the analysis.
""")

# Input section
st.subheader("📝 Enter Your Financial Data")
col1, col2, col3 = st.columns(3)

with col1:
    revenue = st.number_input(
        "Revenue per unit ($)",
        min_value=0.0,
        value=110.0,
        step=1.0,
        help="The amount of revenue generated per unit"
    )

with col2:
    variable_cost = st.number_input(
        "Variable cost per unit ($)",
        min_value=0.0,
        value=90.0,
        step=1.0,
        help="The variable cost associated with each unit"
    )

with col3:
    fixed_cost = st.number_input(
        "Fixed costs ($)",
        min_value=0.0,
        value=15000.0,
        step=100.0,
        help="Total fixed costs that don't vary with the number of units"
    )

# Validate inputs
if revenue <= 0:
    st.error("Revenue per unit must be greater than 0")
elif variable_cost < 0:
    st.error("Variable cost per unit cannot be negative")
elif variable_cost >= revenue:
    st.error("Variable cost per unit must be less than revenue per unit")
elif fixed_cost < 0:
    st.error("Fixed costs cannot be negative")
else:
    # Calculate and display results
    fig, results = calculate_bep_plotly(revenue, variable_cost, fixed_cost)

    # Display results
    st.subheader("📊 Break-Even Analysis Results")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.metric(
            "Break-even Point (Units)", 
            f"{format_currency(results['bep_units'])} units"
        )
        st.metric(
            "Break-even Sales", 
            f"${format_currency(results['bep_sales'])}"
        )
    
    with col2:
        st.metric(
            "Contribution Margin", 
            f"${format_currency(results['contribution_margin'])} per unit"
        )
        st.metric(
            "Contribution Margin Ratio", 
            f"{format_currency(results['contribution_margin_ratio'])}%"
        )

    # Display the plot
    st.plotly_chart(fig, use_container_width=True)

    # Add explanatory notes
    st.markdown("""
    ### 📌 Understanding the Results
    
    - **Break-even Point**: The point where total revenue equals total costs
    - **Contribution Margin**: Revenue per unit minus variable cost per unit
    - **Contribution Margin Ratio**: Contribution margin as a percentage of revenue
    
    The graph shows:
    - 🔵 Blue line: Revenue
    - 🔴 Red line: Total costs
    - 📊 Red area: Loss region
    - 📈 Green area: Profit region
    """)