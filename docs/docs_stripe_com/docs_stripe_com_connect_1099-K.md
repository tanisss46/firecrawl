# 1099-K form state requirements

## View the state requirements for 1099-K forms.

#### Warning

Some participating State regulatory agencies haven’t fully finalized filing
requirements and requirements remain subject to change for the 2024 tax season.
Updates that occur to this page are automatically reflected in the form status
badges and counts in the tax reporting Dashboard.

For 1099-K forms, the IRS requires filing if, in a calendar year, the gross
amount of total reportable payments exceeds $5,000 and there are more than 0
transactions. Filing requirements for some states might differ from federal
requirements.

We outline state filing requirements for 1099-K forms to help you identify which
[states you can file
directly](https://docs.stripe.com/connect/tax-forms-state-requirements) in your
Dashboard, which states require a state tax registration or withholding ID when
filing, and which states you’re responsible for filing directly with.

#### Warning

If you have done backup withholding or state withholding, you might have
additional reporting requirements with states. We recommend that you consult a
tax advisor.

STATE 1099-K FILING REQUIRED DOES STRIPE FILE FILING DUE DATE* FILING THRESHOLD
IF ISSUED, PROVIDE STATE NUMBER AlabamaState PortalApril 30Same as IRS–AlaskaNo
–

–-–ArizonaIf State WitholdingSame as IRS$0–ArkansasCFSFSame as
IRS$2,500–CaliforniaCFSFSame as IRSSame as IRS–ColoradoIf State WitholdingSame
as IRS$0–ConnecticutState PortalApril 30Same as IRSConnecticut Tax Registration
NumberDelawareNo
–

–-–District of ColumbiaState PortalSame as IRS$600–FloridaState PortalApril
30Same as IRS–GeorgiaState PortalSame as IRSSame as IRS–HawaiiCFSFSame as
IRSSame as IRS–IdahoNo
–

–-–IllinoisState PortalSame as IRS$1,000 and 4 transactions–IndianaIf State
WitholdingSame as IRS$0–IowaIf State WitholdingFebruary 15$0–KansasCFSFSame as
IRSSame as IRSKansas Withholding Tax Account NumberKentuckyIf State
WitholdingSame as IRS$0–LouisianaIf State WitholdingSame as IRS$0–MaineState
Portal–Same as IRS–MarylandState PortalSame as IRS$600Maryland Central
Registration NumberMassachusettsState PortalSame as IRS$600–MichiganNo
–

–-–MinnesotaIf State WitholdingSame as IRS$0–MississippiCFSF–Same as
IRS–MissouriNo
–

–-–MontanaState PortalApril 1$600–NebraskaNo
–

–-–NevadaNo
–

–-–New HampshireNo
–

–-–New JerseyCFSFSame as IRS$1,000–New MexicoNo
–

–-–New YorkState PortalApril 30Same as IRS–North CarolinaState PortalSame as
IRS$600NC Withholding ID Number or EINNorth DakotaIf State WitholdingSame as
IRS$0–OhioNo
–

–-–OklahomaNo
–

–-–OregonState PortalSame as IRSSame as IRS–PennsylvaniaNo
–

–-–Rhode IslandIf State WitholdingSame as IRS$100–South CarolinaIf State
WitholdingSame as IRS$0SC Withholding File Number or EINSouth DakotaNo
–

–-–TennesseeState PortalApril 30Same as IRS–TexasNo
–

–-–UtahIf State WitholdingSame as IRS$0–VermontState PortalApril 30$600Vermont
Withholding Account NumberVirginiaState PortalApril 30$600–WashingtonNo
–

–-–West VirginiaIf State WitholdingSame as IRS$0–WisconsinIf State
WitholdingSame as IRS$0Wisconsin Withholding Tax Number**WyomingNo
–

–-–
*January 22, 2025 is the latest recommended date to file forms with the IRS and
states in your Stripe Dashboard

**If a Wisconsin withholding tax number isn’t provided, Stripe uses the default
value of `036888888888801` instead.

## How to interpret form state requirements

Stripe supports filing in all states that require 1099-K filing and don’t have
withholding-based filing requirements. When you file your 1099-K forms from the
[Tax forms view](https://dashboard.stripe.com/connect/taxes/forms) in the
Dashboard, Stripe submits your forms to the IRS and all qualifying states.

### 1099-K FILING REQUIRED

State PortalStripe submits the forms directly to these states. An additional
state filing fee of 1.49 USD applies per 1099-K form filed directly with state
revenue authorities.
CFSF

States listed as CFSF are part of the Combined Federal / State Filing (CFSF)
program. Forms filed to the IRS are automatically forwarded to the state,
eliminating separate reporting to the participating states. If forms have
already been filed with the IRS, you won’t be charged an additional state filing
fee for filing in these states.

Some states still require direct filing with the state, even though they
participate in the CFSF program. Stripe submits the forms directly to these
states.

If State WithholdingYou’re required to file a 1099-K form with that state only
if you withheld state taxes. In your Dashboard, you can specify the amount
withheld by updating the form and updating the `state_tax_withheld` column. When
you file your 1099-K forms in the Dashboard, we automatically export forms
eligible for state filing and with `state_tax_withheld` so you can file directly
with applicable states.
#### Note

Some forms that appear to be below the federal filing threshold can also appear
as `Ready` or `Needs attention` due to Grouped TINs or state filing thresholds.
[Learn
more](https://docs.stripe.com/connect/file-tax-forms#below-threshold-forms)

### FILING DUE DATE

While the IRS filing deadline for 1099-K forms is March 31 and the IRS deadline
to deliver 1099 forms to your payees is January 31, we coupled filing and
delivery together to streamline the tax reporting process. **January 22, 2025**
is the latest recommended date to file forms with the IRS and states in your
Stripe Dashboard. This guarantees forms are filed with the IRS and a copy is
sent to the recipients before the IRS delivery deadline of January 31.

### STATE NUMBERS

State Tax Registration or Withholding IDs are only required for some states.
After you obtain the registration or withholding ID, add the states in which
you’ll file and the corresponding IDs on the [Tax forms
settings](https://dashboard.stripe.com/settings/connect/tax_forms) page. In the
Dashboard, click **Settings**. On **Product settings**, under **Connect**, click
**Tax form settings**. When filing forms in your Dashboard, you must provide an
appropriate ID in states that require one.

## See also

- [File form with
states](https://docs.stripe.com/connect/tax-forms-state-requirements)
- [Add the state tax Registration or withholding
ID](https://docs.stripe.com/connect/tax-forms-state-requirements#add-state-reg)

## Links

- [states you can file
directly](https://docs.stripe.com/connect/tax-forms-state-requirements)
- [Tax forms view](https://dashboard.stripe.com/connect/taxes/forms)
- [Learn
more](https://docs.stripe.com/connect/file-tax-forms#below-threshold-forms)
- [Tax forms settings](https://dashboard.stripe.com/settings/connect/tax_forms)
- [Add the state tax Registration or withholding
ID](https://docs.stripe.com/connect/tax-forms-state-requirements#add-state-reg)