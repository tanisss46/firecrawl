# 1099-NEC form state requirements

## View the state requirements for 1099-NEC forms.

#### Warning

Some participating State regulatory agencies haven’t fully finalized filing
requirements and requirements remain subject to change for the 2024 tax season.
Updates that occur to this page are automatically reflected in the form status
badges and counts in the tax reporting Dashboard.

For 1099-NEC forms, the IRS requires filing if the amount of total reportable
payments is $600 or more. Filing requirements for some states might differ from
federal requirements.

We outline state filing requirements for 1099-NEC forms to help you identify
which [states you can file
directly](https://docs.stripe.com/connect/tax-forms-state-requirements) in your
Dashboard, which states require a state tax registration or withholding ID when
filing, and which states you’re responsible for filing directly with.

#### Warning

If you have done backup withholding or state withholding, you might have
additional reporting requirements with states. We recommend that you consult a
tax advisor.

STATE 1099-NEC FILING REQUIRED DOES STRIPE FILE FILING DUE DATE* FILING
THRESHOLD IF ISSUED, PROVIDE STATE NUMBER AlabamaIf State WitholdingSame as
IRS$0–AlaskaNo
–

–-–ArizonaIf State WitholdingSame as IRS$0–ArkansasCFSFSame as IRSSame as
IRS–CaliforniaCFSFSame as IRSSame as IRS–ColoradoIf State WitholdingMarch
31$0–ConnecticutIf State WitholdingSame as IRS$0Connecticut Tax Registration
NumberDelawareState PortalSame as IRSSame as IRSMust use EINDistrict of
ColumbiaState PortalSame as IRSSame as IRS–FloridaNo
–

–-–GeorgiaIf State WitholdingSame as IRSSame as IRS–HawaiiCFSFSame as IRSSame as
IRS–IdahoCFSFFebruary 28Same as IRSIdaho Withholding Account NumberIllinoisNo
–

–-–IndianaIf State WitholdingSame as IRS$0–IowaIf State WitholdingFebruary
15$0–KansasIf State WitholdingSame as IRS$0Kansas Withholding Tax Account
NumberKentuckyIf State WitholdingSame as IRS$0–LouisianaIf State WitholdingSame
as IRS$0–MaineState Portal–Same as IRS–MarylandIf State WitholdingSame as
IRS$0Maryland Central Registration NumberMassachusettsState PortalSame as
IRSSame as IRS–MichiganIf State WitholdingSame as IRS$0–MinnesotaIf State
WitholdingSame as IRS$0–MississippiIf State WitholdingFebruary
28$0–MissouriCFSFSame as IRSSame as IRS–MontanaState PortalSame as IRSSame as
IRS–NebraskaIf State WitholdingSame as IRS$0Nebraska NumberNevadaNo
–

–-–New HampshireNo
–

–-–New JerseyCFSFSame as IRSSame as IRS–New MexicoNo
–

–-–New YorkNo
–

–-–North CarolinaIf State WitholdingSame as IRS$0NC Withholding ID Number or
EINNorth DakotaIf State WitholdingSame as IRS$0–OhioIf State WitholdingSame as
IRS$0–OklahomaCFSFSame as IRSSame as IRS–OregonState PortalSame as IRSSame as
IRS–PennsylvaniaState PortalSame as IRSSame as IRSPA Employer Account IDRhode
IslandIf State WitholdingSame as IRS$100–South CarolinaIf State WitholdingSame
as IRS$0SC Withholding File Number or EINSouth DakotaNo
–

–-–TennesseeNo
–

–-–TexasNo
–

–-–UtahIf State WitholdingSame as IRS$0–VermontIf State WitholdingSame as
IRS$0Vermont Withholding Account NumberVirginiaIf State WitholdingSame as
IRS$0–WashingtonNo
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

Stripe supports filing in all states that require 1099-NEC filing and don’t have
withholding-based filing requirements. When you file your 1099-NEC forms from
the [Tax forms view](https://dashboard.stripe.com/connect/taxes/forms) in the
Dashboard, Stripe submits your forms to the IRS and all qualifying states.

### 1099-NEC FILING REQUIRED

State PortalStripe submits the forms directly to these states. An additional
state filing fee of 1.49 USD applies per 1099-NEC form filed directly with state
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

If State WithholdingYou’re required to file a 1099-NEC form with that state only
if you withheld state taxes. In your Dashboard, you can specify the amount
withheld by updating the form and updating the `state_tax_withheld` column. When
you file your 1099-NEC forms in the Dashboard, we automatically export forms
eligible for state filing and with `state_tax_withheld` so you can file directly
with applicable states.
#### Note

Some forms that appear to be below the federal filing threshold can also appear
as `Ready` or `Needs attention` due to Grouped TINs or state filing thresholds.
[Learn
more](https://docs.stripe.com/connect/file-tax-forms#below-threshold-forms)

### FILING DUE DATE

While the IRS deadline to file 1099-NEC forms and deliver forms to your payees
is January 31, we coupled filing and delivery together to streamline the
process. **January 22, 2025** is the latest recommended date to file forms with
the IRS and states in your Stripe Dashboard. This guarantees forms are filed
with the IRS and a copy is sent to the recipients before the IRS delivery
deadline of January 31.

### STATE NUMBERS

Some states require State Tax Registration or Withholding IDs. Delaware and
Pennsylvania typically reject state filings for 1099-NEC, when state IDs are
missing and a state ID was issued. After you obtain the registration or
withholding ID, add the states in which you’ll file and the corresponding IDs on
the [Tax forms
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