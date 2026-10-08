# Tailwind CSS Master Cheat Sheet

**The Practical Frontend Developer Reference**  
**Tailwind CSS + React**

**Idea from Ks Shafin** | GitHub: [github.com/KsShafin18](https://github.com/KsShafin18) | Instagram: the_ks_shafin | Facebook: Ks Shafin

> **Version documented: Tailwind CSS v4.3 (v4.x series).** Modern v4 syntax is used throughout. Wherever v3 differs you will find a **Tailwind v3 note**.
> Use **Ctrl+F** to search any class name, CSS property, or phrase such as `I want to center`.
> In VS Code, press **Ctrl+Shift+V** (or **Cmd+Shift+V**) to open the Markdown preview, and click any Table of Contents link to jump.

## How To Use This Reference

| If you know... | Go to |
|---|---|
| The **CSS** you want | Section 32 (CSS to Tailwind conversion table) |
| The **effect** you want ("center", "hide", "shadow") | Section 33 (I Want To Do X quick finder) |
| The **class prefix** but forget the values | Section 35 (cheat tables) |
| How a class name is built | Sections 1 and 34 |
| A bug where a class does nothing | Section 36 (common mistakes) |
| Ready-made components | Section 31 (UI patterns) |
| React specifics | Section 37 |

## Table of Contents

- [1. Tailwind Fundamentals](#1-tailwind-fundamentals)
  - [1.1 What Tailwind CSS Is](#11-what-tailwind-css-is)
  - [1.2 The Utility-First Concept](#12-the-utility-first-concept)
  - [1.3 Documented Version and Setup](#13-documented-version-and-setup)
  - [1.4 How Tailwind Class Names Are Constructed](#14-how-tailwind-class-names-are-constructed)
  - [1.5 How To Understand A Class Without Memorizing It](#15-how-to-understand-a-class-without-memorizing-it)
  - [1.6 Common Naming Patterns](#16-common-naming-patterns)
  - [1.7 Responsive Prefixes (Overview)](#17-responsive-prefixes-overview)
  - [1.8 State Variants (Overview)](#18-state-variants-overview)
  - [1.9 Arbitrary Values (Overview)](#19-arbitrary-values-overview)
  - [1.10 Arbitrary Properties (Overview)](#110-arbitrary-properties-overview)
  - [1.11 Theme Variables (the v4 way to customize)](#111-theme-variables-the-v4-way-to-customize)
  - [1.12 Tailwind v3 vs v4: What Changed (Cheat List)](#112-tailwind-v3-vs-v4-what-changed-cheat-list)
- [2. Spacing System](#2-spacing-system)
  - [2.1 How the Spacing Scale Works](#21-how-the-spacing-scale-works)
  - [2.2 Margin](#22-margin)
  - [2.3 Padding](#23-padding)
  - [2.4 Auto Margins (the centering and pushing tool)](#24-auto-margins-the-centering-and-pushing-tool)
  - [2.5 Negative Spacing](#25-negative-spacing)
  - [2.6 Gap (the modern way to space children)](#26-gap-the-modern-way-to-space-children)
  - [2.7 space-x and space-y](#27-space-x-and-space-y)
  - [2.8 Practical Spacing Examples](#28-practical-spacing-examples)
- [3. Width & Height](#3-width--height)
  - [3.1 Width](#31-width)
  - [3.2 Height](#32-height)
  - [3.3 Min / Max Width and Height](#33-min--max-width-and-height)
  - [3.4 size-* (width and height together)](#34-size--width-and-height-together)
  - [3.5 Practical Width and Height Examples](#35-practical-width-and-height-examples)
- [4. Typography](#4-typography)
  - [4.1 Font Family](#41-font-family)
  - [4.2 Font Size (and its built-in line height)](#42-font-size-and-its-built-in-line-height)
  - [4.3 Font Weight](#43-font-weight)
  - [4.4 Font Style and Smoothing](#44-font-style-and-smoothing)
  - [4.5 Text Alignment](#45-text-alignment)
  - [4.6 Line Height (leading)](#46-line-height-leading)
  - [4.7 Letter Spacing (tracking)](#47-letter-spacing-tracking)
  - [4.8 Text Decoration](#48-text-decoration)
  - [4.9 Text Transform](#49-text-transform)
  - [4.10 Text Overflow, Truncation and Line Clamp](#410-text-overflow-truncation-and-line-clamp)
  - [4.11 Whitespace](#411-whitespace)
  - [4.12 Word Breaking and Wrapping](#412-word-breaking-and-wrapping)
  - [4.13 More Typography Utilities](#413-more-typography-utilities)
  - [4.14 Practical Typography Recipes](#414-practical-typography-recipes)
- [5. Colors](#5-colors)
  - [5.1 The Color Scale](#51-the-color-scale)
  - [5.2 Color Utilities (every place a color can go)](#52-color-utilities-every-place-a-color-can-go)
  - [5.3 Color Opacity (the slash syntax)](#53-color-opacity-the-slash-syntax)
  - [5.4 Special Color Keywords](#54-special-color-keywords)
  - [5.5 Arbitrary Colors](#55-arbitrary-colors)
  - [5.6 Defining Your Own Colors (v4)](#56-defining-your-own-colors-v4)
  - [5.7 Color Mixing Examples](#57-color-mixing-examples)
- [6. Backgrounds](#6-backgrounds)
  - [6.1 Background Color](#61-background-color)
  - [6.2 Background Image](#62-background-image)
  - [6.3 Background Size](#63-background-size)
  - [6.4 Background Position](#64-background-position)
  - [6.5 Background Repeat](#65-background-repeat)
  - [6.6 Background Attachment](#66-background-attachment)
  - [6.7 Background Clip and Origin](#67-background-clip-and-origin)
  - [6.8 Gradients](#68-gradients)
  - [6.9 Practical Background Recipes](#69-practical-background-recipes)
- [7. Borders & Radius](#7-borders--radius)
  - [7.1 Border Width](#71-border-width)
  - [7.2 Border Color and Opacity](#72-border-color-and-opacity)
  - [7.3 Border Style](#73-border-style)
  - [7.4 Divide (borders between children)](#74-divide-borders-between-children)
  - [7.5 Outline and Ring](#75-outline-and-ring)
  - [7.6 Border Radius](#76-border-radius)
  - [7.7 Individual Corners and Sides](#77-individual-corners-and-sides)
- [8. Shadows & Effects](#8-shadows--effects)
  - [8.1 Box Shadow](#81-box-shadow)
  - [8.2 Opacity](#82-opacity)
  - [8.3 Blend Modes](#83-blend-modes)
  - [8.4 Box Decoration Break](#84-box-decoration-break)
  - [8.5 Isolation (stacking contexts)](#85-isolation-stacking-contexts)
  - [8.6 Masks (v4.1+)](#86-masks-v41)
- [9. Flexbox](#9-flexbox)
  - [9.1 The Mental Model: Main Axis and Cross Axis](#91-the-mental-model-main-axis-and-cross-axis)
  - [9.2 Flex Container](#92-flex-container)
  - [9.3 Justify Content (main axis)](#93-justify-content-main-axis)
  - [9.4 Align Items (cross axis)](#94-align-items-cross-axis)
  - [9.5 Align Content (multi-line flex only)](#95-align-content-multi-line-flex-only)
  - [9.6 Align Self (one item overrides `items-*`)](#96-align-self-one-item-overrides-items-)
  - [9.7 Flex Item Sizing: flex, grow, shrink, basis](#97-flex-item-sizing-flex-grow-shrink-basis)
  - [9.8 Practical Flexbox Recipes](#98-practical-flexbox-recipes)
- [10. CSS Grid](#10-css-grid)
  - [10.1 Grid Container](#101-grid-container)
  - [10.2 Grid Items: Spanning and Placement](#102-grid-items-spanning-and-placement)
  - [10.3 Auto Flow and Auto Tracks](#103-auto-flow-and-auto-tracks)
  - [10.4 Alignment in Grid](#104-alignment-in-grid)
  - [10.5 Practical Grid Layouts](#105-practical-grid-layouts)
- [11. Positioning](#11-positioning)
  - [11.1 Position Types](#111-position-types)
  - [11.2 Inset (top, right, bottom, left)](#112-inset-top-right-bottom-left)
  - [11.3 Z-Index](#113-z-index)
  - [11.4 Positioning Recipes](#114-positioning-recipes)
- [12. Display](#12-display)
- [13. Overflow](#13-overflow)
- [14. Object & Image Utilities](#14-object--image-utilities)
  - [14.1 Object Fit](#141-object-fit)
  - [14.2 Object Position](#142-object-position)
  - [14.3 Image Examples](#143-image-examples)
- [15. Aspect Ratio](#15-aspect-ratio)
- [16. Lists](#16-lists)
- [17. Tables](#17-tables)
- [18. Forms / Inputs](#18-forms--inputs)
  - [18.1 Form State Variants](#181-form-state-variants)
  - [18.2 Text Input](#182-text-input)
  - [18.3 Textarea](#183-textarea)
  - [18.4 Select](#184-select)
  - [18.5 Checkbox and Radio](#185-checkbox-and-radio)
  - [18.6 Buttons](#186-buttons)
  - [18.7 File Input](#187-file-input)
  - [18.8 Range, Switch and Misc](#188-range-switch-and-misc)
  - [18.9 Complete Form Example](#189-complete-form-example)
- [19. Interactivity](#19-interactivity)
  - [19.1 Cursor](#191-cursor)
  - [19.2 Pointer Events, User Select, Resize, Appearance](#192-pointer-events-user-select-resize-appearance)
  - [19.3 Scroll Behavior and Snap](#193-scroll-behavior-and-snap)
  - [19.4 Caret and Accent](#194-caret-and-accent)
- [20. Transitions & Animation](#20-transitions--animation)
  - [20.1 Transition Property](#201-transition-property)
  - [20.2 Duration, Timing, Delay](#202-duration-timing-delay)
  - [20.3 Built-in Animations](#203-built-in-animations)
  - [20.4 Custom Animations (concept)](#204-custom-animations-concept)
  - [20.5 Animation Accessibility and Entry Animations](#205-animation-accessibility-and-entry-animations)
- [21. Transform](#21-transform)
  - [21.1 Scale, Rotate, Translate, Skew](#211-scale-rotate-translate-skew)
  - [21.2 Transform Origin](#212-transform-origin)
  - [21.3 3D Transforms (v4)](#213-3d-transforms-v4)
  - [21.4 Transform Recipes](#214-transform-recipes)
- [22. Filters & Visual Effects](#22-filters--visual-effects)
  - [22.1 Filter Utilities (apply to the element)](#221-filter-utilities-apply-to-the-element)
  - [22.2 Backdrop Filters (affect what is behind the element)](#222-backdrop-filters-affect-what-is-behind-the-element)
  - [22.3 Glassmorphism Examples](#223-glassmorphism-examples)
- [23. Responsive Design](#23-responsive-design)
  - [23.1 Mobile-First: The Key Idea](#231-mobile-first-the-key-idea)
  - [23.2 Breakpoints](#232-breakpoints)
  - [23.3 Max-Width Variants and Ranges](#233-max-width-variants-and-ranges)
  - [23.4 Container Queries (v4 built-in)](#234-container-queries-v4-built-in)
  - [23.5 Custom Breakpoints](#235-custom-breakpoints)
  - [23.6 Responsive Patterns](#236-responsive-patterns)
- [24. State Variants](#24-state-variants)
  - [24.1 Interaction States](#241-interaction-states)
  - [24.2 Form States](#242-form-states)
  - [24.3 Structural (position in the DOM)](#243-structural-position-in-the-dom)
  - [24.4 Pseudo-elements](#244-pseudo-elements)
  - [24.5 Attribute, Media and Other Variants](#245-attribute-media-and-other-variants)
  - [24.6 Practical State Examples](#246-practical-state-examples)
- [25. Group & Peer](#25-group--peer)
  - [25.1 Group: style children based on the PARENT'S state](#251-group-style-children-based-on-the-parents-state)
  - [25.2 Peer: style an element based on a SIBLING'S state](#252-peer-style-an-element-based-on-a-siblings-state)
- [26. Dark Mode](#26-dark-mode)
  - [26.1 The dark: Variant](#261-the-dark-variant)
  - [26.2 How Dark Mode Works in v4](#262-how-dark-mode-works-in-v4)
  - [26.3 React Dark Mode Toggle](#263-react-dark-mode-toggle)
  - [26.4 Dark Mode Tips](#264-dark-mode-tips)
- [27. Arbitrary Values](#27-arbitrary-values)
  - [27.1 Arbitrary Values `utility-[value]`](#271-arbitrary-values-utility-value)
  - [27.2 Arbitrary Properties `[property:value]`](#272-arbitrary-properties-propertyvalue)
  - [27.3 Arbitrary Variants `[selector]:`](#273-arbitrary-variants-selector)
  - [27.4 When to Use (and Not Use) Arbitrary Values](#274-when-to-use-and-not-use-arbitrary-values)
- [28. Important Modifier](#28-important-modifier)
- [29. Container](#29-container)
  - [29.1 The container Class](#291-the-container-class)
  - [29.2 Customize the container (v4)](#292-customize-the-container-v4)
- [30. Accessibility](#30-accessibility)
  - [30.1 Screen Reader Utilities](#301-screen-reader-utilities)
  - [30.2 Focus States (never remove them without a replacement)](#302-focus-states-never-remove-them-without-a-replacement)
  - [30.3 Accessible Buttons and Forms Checklist](#303-accessible-buttons-and-forms-checklist)
- [31. Common UI Patterns](#31-common-ui-patterns)
  - [31.1 Navbar](#311-navbar)
  - [31.2 Hero Section](#312-hero-section)
  - [31.3 Profile Card](#313-profile-card)
  - [31.4 Product Card](#314-product-card)
  - [31.5 Login Form](#315-login-form)
  - [31.6 Signup Form](#316-signup-form)
  - [31.7 Button Variants](#317-button-variants)
  - [31.8 Modal](#318-modal)
  - [31.9 Dropdown](#319-dropdown)
  - [31.10 Sidebar](#3110-sidebar)
  - [31.11 Dashboard Layout](#3111-dashboard-layout)
  - [31.12 Pricing Card](#3112-pricing-card)
  - [31.13 Alert](#3113-alert)
  - [31.14 Badge](#3114-badge)
  - [31.15 Loading Spinner](#3115-loading-spinner)
  - [31.16 Skeleton Loader](#3116-skeleton-loader)
  - [31.17 Image Gallery](#3117-image-gallery)
  - [31.18 Responsive Grid](#3118-responsive-grid)
  - [31.19 Footer](#3119-footer)
- [32. CSS → Tailwind Conversion Table](#32-css--tailwind-conversion-table)
  - [32.1 Display and Layout](#321-display-and-layout)
  - [32.2 Spacing and Sizing](#322-spacing-and-sizing)
  - [32.3 Flexbox](#323-flexbox)
  - [32.4 Grid](#324-grid)
  - [32.5 Position](#325-position)
  - [32.6 Typography](#326-typography)
  - [32.7 Colors and Backgrounds](#327-colors-and-backgrounds)
  - [32.8 Borders, Radius, Shadows](#328-borders-radius-shadows)
  - [32.9 Overflow, Objects, Interactivity](#329-overflow-objects-interactivity)
  - [32.10 Transitions, Transforms, Filters](#3210-transitions-transforms-filters)
  - [32.11 Media Queries and Pseudo-classes](#3211-media-queries-and-pseudo-classes)
- [33. "I Want To Do X" Quick Finder](#33-i-want-to-do-x-quick-finder)
  - [33.1 Layout](#331-layout)
  - [33.2 Visibility and Responsive](#332-visibility-and-responsive)
  - [33.3 Shape, Borders, Shadows](#333-shape-borders-shadows)
  - [33.4 Color and Background](#334-color-and-background)
  - [33.5 Text](#335-text)
  - [33.6 Interaction and Animation](#336-interaction-and-animation)
  - [33.7 Images, Forms, Misc](#337-images-forms-misc)
- [34. Class Name Construction Guide](#34-class-name-construction-guide)
  - [34.1 The Recipe](#341-the-recipe)
  - [34.2 Worked Example: Heading](#342-worked-example-heading)
  - [34.3 Worked Example: Card](#343-worked-example-card)
  - [34.4 Worked Example: Centered Flex Row](#344-worked-example-centered-flex-row)
  - [34.5 Worked Example: Button](#345-worked-example-button)
  - [34.6 Worked Example: Absolutely Positioned Badge](#346-worked-example-absolutely-positioned-badge)
  - [34.7 Worked Example: Responsive Grid](#347-worked-example-responsive-grid)
  - [34.8 Quick Property-to-Prefix Dictionary](#348-quick-property-to-prefix-dictionary)
- [35. Tailwind Cheat Tables](#35-tailwind-cheat-tables)
  - [35.1 Typography](#351-typography)
  - [35.2 Spacing](#352-spacing)
  - [35.3 Colors](#353-colors)
  - [35.4 Width](#354-width)
  - [35.5 Height](#355-height)
  - [35.6 Flex](#356-flex)
  - [35.7 Grid](#357-grid)
  - [35.8 Position](#358-position)
  - [35.9 Border](#359-border)
  - [35.10 Radius](#3510-radius)
  - [35.11 Shadow](#3511-shadow)
  - [35.12 Responsive](#3512-responsive)
  - [35.13 States](#3513-states)
  - [35.14 Animation and Transition](#3514-animation-and-transition)
  - [35.15 Transform](#3515-transform)
  - [35.16 Effects and Filters](#3516-effects-and-filters)
- [36. Common Mistakes](#36-common-mistakes)
  - [36.1 Using Invalid Class Names](#361-using-invalid-class-names)
  - [36.2 Forgetting Mobile-First Behavior](#362-forgetting-mobile-first-behavior)
  - [36.3 Confusing justify-* and items-*](#363-confusing-justify--and-items-)
  - [36.4 Overusing Arbitrary Values](#364-overusing-arbitrary-values)
  - [36.5 Incorrect Responsive Classes](#365-incorrect-responsive-classes)
  - [36.6 Tailwind v3 vs v4 Confusion](#366-tailwind-v3-vs-v4-confusion)
  - [36.7 Dynamic Class Names Tailwind Cannot Detect](#367-dynamic-class-names-tailwind-cannot-detect)
  - [36.8 Missing Source Detection / Configuration](#368-missing-source-detection--configuration)
  - [36.9 Using @apply Unnecessarily](#369-using-apply-unnecessarily)
  - [36.10 Specificity and Override Problems](#3610-specificity-and-override-problems)
  - [36.11 Important Modifier Misuse](#3611-important-modifier-misuse)
  - [36.12 Other Frequent Mistakes](#3612-other-frequent-mistakes)
- [37. React + Tailwind Notes](#37-react--tailwind-notes)
  - [37.1 className, Not class](#371-classname-not-class)
  - [37.2 Conditional Classes: Ternary](#372-conditional-classes-ternary)
  - [37.3 Template Literals (for combining static + conditional)](#373-template-literals-for-combining-static--conditional)
  - [37.4 clsx (clean conditional classes)](#374-clsx-clean-conditional-classes)
  - [37.5 tailwind-merge and the cn() Helper](#375-tailwind-merge-and-the-cn-helper)
  - [37.6 Variant Maps (safe dynamic styling)](#376-variant-maps-safe-dynamic-styling)
  - [37.7 Reusable Component Styling](#377-reusable-component-styling)
  - [37.8 Styling by State with Data Attributes](#378-styling-by-state-with-data-attributes)
  - [37.9 Truly Dynamic Values](#379-truly-dynamic-values)
  - [37.10 Lists, Mapping and Layout in React](#3710-lists-mapping-and-layout-in-react)
  - [37.11 Handy React + Tailwind Checklist](#3711-handy-react--tailwind-checklist)
- [Appendix: Mental Checklist When Styling Anything](#appendix-mental-checklist-when-styling-anything)

---

## 1. Tailwind Fundamentals

### 1.1 What Tailwind CSS Is

Tailwind CSS is a **utility-first CSS framework**. Instead of writing CSS in a separate file and inventing class names like `.card-title`, you compose your design directly in your markup using small, single-purpose classes.

```html
<!-- Traditional CSS -->
<h2 class="card-title">Hello</h2>
<style>
  .card-title { font-size: 1.5rem; font-weight: 700; color: #3b82f6; }
</style>

<!-- Tailwind -->
<h2 class="text-2xl font-bold text-blue-500">Hello</h2>
```

Why people like it:

- **No naming things.** You never invent `.wrapper-inner-2` again.
- **No context switching.** Style and structure live in the same file (perfect for React components).
- **Consistent design.** Spacing, colors and font sizes come from a shared scale, so designs look cohesive.
- **Small CSS output.** Tailwind only generates the CSS for classes you actually use.
- **Responsive and state styling is built in** (`md:`, `hover:`, `dark:`).

### 1.2 The Utility-First Concept

One class = one (or a few) CSS declaration(s). You combine many small classes to build a design.

| Class | CSS it generates |
|---|---|
| `p-4` | `padding: 1rem` |
| `text-xl` | `font-size: 1.25rem; line-height: 1.75rem` |
| `font-bold` | `font-weight: 700` |
| `bg-blue-500` | `background-color: <blue 500>` |
| `rounded-lg` | `border-radius: 0.5rem` |
| `flex` | `display: flex` |

### 1.3 Documented Version and Setup

> **Version documented: Tailwind CSS v4.3 (v4.x series).** Everything in this manual targets v4 syntax. Where v3 differs, you will see a **Tailwind v3 note**.

Minimum browser support for v4: Safari 16.4+, Chrome 111+, Firefox 128+ (it relies on modern CSS such as `@property` and `color-mix()`). If you must support older browsers, stay on Tailwind v3.4.

**Quick setup: React + Vite (Tailwind v4)**

```bash
npm create vite@latest my-app -- --template react
cd my-app
npm install tailwindcss @tailwindcss/vite
```

```js
// vite.config.js
import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'
import tailwindcss from '@tailwindcss/vite'

export default defineConfig({
  plugins: [react(), tailwindcss()],
})
```

```css
/* src/index.css */
@import "tailwindcss";
```

```jsx
// src/App.jsx
export default function App() {
  return <h1 className="text-3xl font-bold underline">Hello Tailwind</h1>
}
```

Make sure `index.css` is imported in `main.jsx` (`import './index.css'`). There is **no** `tailwind.config.js` and **no** `content` array needed in v4 by default: Tailwind scans your project automatically.

> **Tailwind v3 note:** v3 used `@tailwind base; @tailwind components; @tailwind utilities;`, a `tailwind.config.js` file with a `content: [...]` array, and PostCSS + autoprefixer. In v4 you write `@import "tailwindcss";` and configure the theme in CSS with `@theme`.

**Recommended tools**

- **Tailwind CSS IntelliSense** (VS Code extension): autocomplete, hover previews of the CSS behind each class, and lint warnings for invalid classes.
- **prettier-plugin-tailwindcss**: automatically sorts classes into a consistent order.

### 1.4 How Tailwind Class Names Are Constructed

Almost every class follows this pattern:

```text
[variants:] [-] utility - value [/ modifier] [!]
```

| Part | Meaning | Example |
|---|---|---|
| variants | Conditions: screen size, hover, dark mode... (separated by `:`) | `md:hover:` |
| `-` (leading) | Negative value | `-mt-4` |
| utility | Which CSS property family | `bg`, `text`, `p`, `w`, `border` |
| value | From the theme scale, or arbitrary `[...]` | `blue-500`, `4`, `lg`, `[350px]` |
| `/modifier` | Opacity, line-height or a fraction | `bg-black/50`, `text-xl/8`, `w-1/2` |
| `!` (trailing) | Important | `p-4!` |

**Worked examples**

| Class | Breakdown |
|---|---|
| `text-xl` | utility `text` (font size) + value `xl` |
| `font-bold` | utility `font` (weight) + value `bold` |
| `bg-blue-500` | utility `bg` (background color) + color `blue` + shade `500` |
| `p-4` | utility `p` (padding) + scale value `4` (= 1rem) |
| `mt-6` | `m` (margin) + `t` (top) + `6` (= 1.5rem) |
| `rounded-lg` | utility `rounded` (border radius) + size `lg` |
| `shadow-md` | utility `shadow` + size `md` |
| `md:hover:bg-red-500` | at `md` screens and up, on hover, background red 500 |
| `-translate-y-1` | negative translate on Y axis |
| `w-[350px]` | width with an arbitrary value |

### 1.5 How To Understand A Class Without Memorizing It

Use this three-step method every time:

1. **Name the CSS property** you want (for example `margin-top`).
2. **Take its Tailwind prefix** (`margin` becomes `m`; `top` becomes `t`; so `mt`).
3. **Add the value** from the scale (`mt-4`) or an arbitrary one (`mt-[37px]`).

### 1.6 Common Naming Patterns

| Pattern | Meaning | Examples |
|---|---|---|
| Shorthand prefix | First letters of the CSS property | `m` margin, `p` padding, `w` width, `h` height, `bg` background |
| Side suffix | `t` top, `r` right, `b` bottom, `l` left | `mt-4`, `pr-2`, `border-b` |
| Axis suffix | `x` horizontal, `y` vertical | `px-4`, `my-2`, `translate-x-2` |
| Logical sides | `s` start, `e` end (RTL friendly) | `ps-4`, `me-2`, `border-s` |
| Scale numbers | Number x 0.25rem (4px) | `p-1`=4px, `p-4`=16px, `p-8`=32px |
| T-shirt sizes | `xs sm md lg xl 2xl 3xl...` | `text-lg`, `shadow-xl`, `rounded-2xl` |
| Fractions | Percent widths | `w-1/2`, `w-2/3`, `basis-1/4` |
| Keywords | CSS keywords | `w-full`, `w-auto`, `h-screen`, `w-fit` |
| Color + shade | `{color}-{50..950}` | `text-gray-700`, `bg-red-500` |
| Negative | Leading dash | `-mt-4`, `-rotate-45`, `-inset-2` |
| Opacity slash | `/{0-100}` | `bg-blue-500/50` |
| Axis-specific split | Property family + direction | `overflow-x-auto`, `gap-y-4` |

### 1.7 Responsive Prefixes (Overview)

Prefix any utility with a breakpoint name to apply it **at that width and above** (mobile-first):

```html
<div class="text-sm md:text-lg lg:text-2xl">
  Small on mobile, large from 768px, even larger from 1024px
</div>
```

| Prefix | Min width | CSS |
|---|---|---|
| (none) | 0 | applies to all sizes |
| `sm:` | 640px (40rem) | `@media (min-width: 40rem)` |
| `md:` | 768px (48rem) | `@media (min-width: 48rem)` |
| `lg:` | 1024px (64rem) | `@media (min-width: 64rem)` |
| `xl:` | 1280px (80rem) | `@media (min-width: 80rem)` |
| `2xl:` | 1536px (96rem) | `@media (min-width: 96rem)` |

Full details are in [Section 23](#23-responsive-design).

### 1.8 State Variants (Overview)

Prefix a utility with a state to apply it only in that state:

```html
<button class="bg-blue-500 hover:bg-blue-600 focus:ring-2 active:scale-95 disabled:opacity-50">
  Click me
</button>
```

Variants can be stacked; they apply **left to right**: `md:hover:bg-red-500` means "at md and up, when hovered". Full details are in [Section 24](#24-state-variants).

### 1.9 Arbitrary Values (Overview)

When the theme scale does not contain the value you need, put any CSS value in square brackets:

```html
<div class="w-[350px] mt-[37px] bg-[#1e293b] text-[22px] grid-cols-[200px_1fr]"></div>
```

- Use `_` instead of spaces: `grid-cols-[200px_1fr]` becomes `200px 1fr`.
- Works with variants: `md:w-[500px]`, `hover:bg-[#123456]`.

Full details are in [Section 27](#27-arbitrary-values).

### 1.10 Arbitrary Properties (Overview)

For a CSS property Tailwind has no utility for, write the property itself in brackets:

```html
<div class="[mask-type:luminance] [--my-var:10px] hover:[mask-type:alpha]"></div>
```

Format: `[property:value]`. Works with variants too.

### 1.11 Theme Variables (the v4 way to customize)

In v4 you extend the design system in CSS with `@theme`. Every theme variable automatically creates utilities.

```css
@import "tailwindcss";

@theme {
  --color-brand: oklch(0.65 0.2 260);   /* creates bg-brand, text-brand, border-brand... */
  --font-display: "Poppins", sans-serif; /* creates font-display */
  --breakpoint-3xl: 120rem;              /* creates 3xl: variant */
  --spacing: 0.25rem;                    /* base spacing unit (default) */
}
```

```html
<h1 class="font-display text-brand 3xl:text-6xl">Custom theme</h1>
```

> **Tailwind v3 note:** v3 customized the theme in `tailwind.config.js` under `theme.extend`. In v4 the same data lives in CSS `@theme` blocks. You can still load a JS config with `@config "./tailwind.config.js";` for migration.

### 1.12 Tailwind v3 vs v4: What Changed (Cheat List)

| Topic | Tailwind v3 | Tailwind v4 (use this) |
|---|---|---|
| Import | `@tailwind base; @tailwind components; @tailwind utilities;` | `@import "tailwindcss";` |
| Config | `tailwind.config.js` | CSS `@theme { ... }` |
| Content paths | `content: [...]` required | Automatic detection (`@source` if needed) |
| Gradients | `bg-gradient-to-r` | `bg-linear-to-r` (old name still accepted as a legacy alias) |
| Opacity utilities | `bg-opacity-50`, `text-opacity-50` | Removed: use `bg-black/50`, `text-white/50` |
| Shadow scale | `shadow-sm`, `shadow`, `shadow-md` | `shadow-2xs`, `shadow-xs`, `shadow-sm`, `shadow-md`... (v3 `shadow` = v4 `shadow-sm`; v3 `shadow-sm` = v4 `shadow-xs`) |
| Inner shadow | `shadow-inner` | `inset-shadow-*` |
| Blur scale | `blur-sm`, `blur` | `blur-xs`, `blur-sm`... (v3 `blur` = v4 `blur-sm`) |
| Radius scale | `rounded-sm`, `rounded` | `rounded-xs`, `rounded-sm`... (v3 `rounded` = v4 `rounded-sm`) |
| Ring | `ring` = 3px, default blue | `ring` = 1px, default `currentColor`: use `ring-3` for old width |
| Outline reset | `outline-none` | `outline-hidden` (and `outline-none` now truly sets `outline-style: none`) |
| Default border color | `gray-200` | `currentColor`: always set a color, e.g. `border-gray-200` |
| Flex shrink/grow | `flex-shrink-0`, `flex-grow` | `shrink-0`, `grow` |
| Text overflow | `overflow-ellipsis` | `text-ellipsis` |
| Box decoration | `decoration-clone`, `decoration-slice` | `box-decoration-clone`, `box-decoration-slice` |
| Placeholder color | `placeholder-gray-400` | `placeholder:text-gray-400` (variant) |
| Important | `!font-bold` (prefix) | `font-bold!` (suffix; prefix still works but is legacy) |
| CSS variable value | `bg-[--brand]` | `bg-(--brand)` |
| Stacked variants order | right to left | left to right |
| Dark mode toggle | `darkMode: 'class'` in config | `@custom-variant dark (...)` in CSS |
| Button cursor | `cursor: pointer` by default | `cursor: default`: add `cursor-pointer` yourself |
| `hover:` | Applied on touch devices too | Only when the device supports hover |
| `container` options | `center`, `padding` in config | Customize with `@utility container {...}` |

---

## 2. Spacing System

### 2.1 How the Spacing Scale Works

Tailwind spacing is based on **one unit: `0.25rem` (= 4px at default browser size)**. The number in the class is a **multiplier**:

```text
value  x  0.25rem  =  size
  1    x  0.25rem  =  0.25rem  =  4px
  4    x  0.25rem  =  1rem     =  16px
  8    x  0.25rem  =  2rem     =  32px
```

**Fast mental math:** `class number x 4 = pixels`. So `p-6` = 24px, `mt-10` = 40px.

In v4, **any number works** (`p-13`, `mt-17`), because spacing is computed from the base unit. In v3 only the predefined steps existed. The same scale is used by `w-`, `h-`, `gap-`, `inset-`, `translate-` and more.

| Class value | rem | px | | Class value | rem | px |
|---|---|---|---|---|---|---|
| `0` | 0 | 0 | | `12` | 3 | 48 |
| `px` | 1px | 1 | | `14` | 3.5 | 56 |
| `0.5` | 0.125 | 2 | | `16` | 4 | 64 |
| `1` | 0.25 | 4 | | `20` | 5 | 80 |
| `1.5` | 0.375 | 6 | | `24` | 6 | 96 |
| `2` | 0.5 | 8 | | `28` | 7 | 112 |
| `2.5` | 0.625 | 10 | | `32` | 8 | 128 |
| `3` | 0.75 | 12 | | `40` | 10 | 160 |
| `3.5` | 0.875 | 14 | | `48` | 12 | 192 |
| `4` | 1 | 16 | | `56` | 14 | 224 |
| `5` | 1.25 | 20 | | `64` | 16 | 256 |
| `6` | 1.5 | 24 | | `72` | 18 | 288 |
| `8` | 2 | 32 | | `80` | 20 | 320 |
| `10` | 2.5 | 40 | | `96` | 24 | 384 |

**Everyday values you will use 90% of the time:** `1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24`.

### 2.2 Margin

| CSS Purpose | Tailwind | Example |
|---|---|---|
| margin (all sides) | `m-{n}` | `m-4` |
| margin horizontal (left + right) | `mx-{n}` | `mx-4` |
| margin vertical (top + bottom) | `my-{n}` | `my-4` |
| margin-top | `mt-{n}` | `mt-4` |
| margin-right | `mr-{n}` | `mr-4` |
| margin-bottom | `mb-{n}` | `mb-4` |
| margin-left | `ml-{n}` | `ml-4` |
| margin-inline-start (RTL aware) | `ms-{n}` | `ms-4` |
| margin-inline-end (RTL aware) | `me-{n}` | `me-4` |
| auto margin | `m-auto`, `mx-auto`, `my-auto`, `ml-auto`, `mr-auto` | `mx-auto` |
| negative margin | `-m-{n}`, `-mt-{n}`... | `-mt-4` |
| arbitrary margin | `m-[value]` | `mt-[37px]` |

> **v4.2+:** logical block-axis margin utilities `mbs-{n}` (margin-block-start) and `mbe-{n}` (margin-block-end) also exist (and `pbs-`/`pbe-` for padding). Most people never need them.

### 2.3 Padding

| CSS Purpose | Tailwind | Example |
|---|---|---|
| padding (all sides) | `p-{n}` | `p-4` |
| horizontal padding | `px-{n}` | `px-4` |
| vertical padding | `py-{n}` | `py-4` |
| padding-top | `pt-{n}` | `pt-4` |
| padding-right | `pr-{n}` | `pr-4` |
| padding-bottom | `pb-{n}` | `pb-4` |
| padding-left | `pl-{n}` | `pl-4` |
| padding-inline-start | `ps-{n}` | `ps-4` |
| padding-inline-end | `pe-{n}` | `pe-4` |
| arbitrary padding | `p-[value]` | `px-[18px]` |

Padding **cannot** be `auto` and **cannot** be negative.

### 2.4 Auto Margins (the centering and pushing tool)

```html
<!-- Center a fixed-width block horizontally -->
<div class="mx-auto w-96">Centered</div>

<!-- Push an item to the far right inside a flex row -->
<nav class="flex">
  <a>Logo</a>
  <a class="ml-auto">Login</a>   <!-- takes all free space on its left -->
</nav>

<!-- Center vertically + horizontally inside a flex parent -->
<div class="flex h-screen"><div class="m-auto">Centered</div></div>
```

### 2.5 Negative Spacing

Put a `-` **in front of the utility**: `-mt-4`, `-ml-2`, `-m-1`. Also works for `inset`, `translate`, `rotate`, `skew`, `scale` and others.

```html
<img class="-mt-12 rounded-full" />        <!-- pull avatar upward over a banner -->
<div class="-mx-4 px-4">Full-bleed row</div> <!-- cancel parent's horizontal padding -->
```

### 2.6 Gap (the modern way to space children)

`gap` works on **flex and grid** parents and puts space **between** children (not outside).

| CSS Purpose | Tailwind | Example |
|---|---|---|
| gap (row + column) | `gap-{n}` | `gap-4` |
| column-gap | `gap-x-{n}` | `gap-x-6` |
| row-gap | `gap-y-{n}` | `gap-y-2` |

```html
<div class="flex gap-4">...</div>
<div class="grid grid-cols-3 gap-x-6 gap-y-2">...</div>
```

### 2.7 space-x and space-y

Adds margin between **direct children** of any container (no flex or grid needed).

| Class | Effect |
|---|---|
| `space-x-{n}` | horizontal space between children |
| `space-y-{n}` | vertical space between children |
| `space-x-reverse`, `space-y-reverse` | use with `flex-row-reverse` / `flex-col-reverse` |
| `-space-x-{n}` | negative space (overlapping avatars) |

```html
<ul class="space-y-2">         <!-- 8px between list items -->
  <li>One</li><li>Two</li><li>Three</li>
</ul>

<div class="flex -space-x-2">  <!-- overlapping avatar stack -->
  <img class="size-8 rounded-full ring-2 ring-white" src="a.jpg" />
  <img class="size-8 rounded-full ring-2 ring-white" src="b.jpg" />
</div>
```

> **Prefer `gap-*`** with flex and grid: it behaves better with wrapping and with hidden children. Use `space-*` for simple stacks or when you cannot use flex/grid.

### 2.8 Practical Spacing Examples

```html
<!-- Card with comfortable padding and spaced contents -->
<div class="p-6 space-y-3 rounded-xl border border-gray-200">
  <h3 class="text-lg font-semibold">Title</h3>
  <p class="text-gray-600">Description</p>
  <button class="mt-2 px-4 py-2 bg-blue-500 text-white rounded-lg">Action</button>
</div>

<!-- Page section: vertical rhythm -->
<section class="py-16 md:py-24 px-4">...</section>

<!-- Button spacing: px bigger than py looks balanced -->
<button class="px-6 py-3">...</button>
```

---

## 3. Width & Height

### 3.1 Width

| CSS | Tailwind | Notes |
|---|---|---|
| `width: 1rem` etc. | `w-4`, `w-10`, `w-64` | spacing scale (n x 0.25rem) |
| `width: 1px` | `w-px` | |
| `width: 50%` | `w-1/2` | fractions: `1/2`, `1/3`, `2/3`, `1/4`, `3/4`, `1/5`... `11/12` |
| `width: 100%` | `w-full` | fills parent |
| `width: 100vw` | `w-screen` | viewport width (can cause horizontal scroll) |
| `width: 100dvw / svw / lvw` | `w-dvw`, `w-svw`, `w-lvw` | dynamic / small / large viewport |
| `width: auto` | `w-auto` | |
| `width: fit-content` | `w-fit` | shrink to content |
| `width: min-content` | `w-min` | |
| `width: max-content` | `w-max` | |
| container sizes | `w-3xs`, `w-xs`, `w-sm`, `w-md`, `w-lg`, `w-xl`, `w-2xl` ... `w-7xl` | v4: named sizes usable on `w-` too |
| arbitrary | `w-[350px]`, `w-[50vw]`, `w-[calc(100%-2rem)]` | |
| CSS variable | `w-(--sidebar-width)` | v4 syntax |

### 3.2 Height

| CSS | Tailwind | Notes |
|---|---|---|
| `height: n` | `h-4`, `h-10`, `h-64` | spacing scale |
| `height: 100%` | `h-full` | parent needs a defined height |
| `height: 100vh` | `h-screen` | viewport height |
| `100dvh / svh / lvh` | `h-dvh`, `h-svh`, `h-lvh` | mobile-friendly viewport units |
| `height: auto` | `h-auto` | |
| `fit-content / min-content / max-content` | `h-fit`, `h-min`, `h-max` | |
| fractions | `h-1/2`, `h-1/3` | needs parent with height |
| arbitrary | `h-[500px]`, `h-[calc(100vh-4rem)]` | |

> **Mobile tip:** `h-screen` (100vh) can be taller than the visible area on mobile browsers because of the address bar. Prefer **`h-dvh`** / **`min-h-dvh`** for full-screen mobile layouts.

### 3.3 Min / Max Width and Height

| CSS | Tailwind |
|---|---|
| `min-width: 0` | `min-w-0` (important to let flex children shrink and truncate) |
| `min-width: 100%` | `min-w-full` |
| `min-width: min-content / max-content / fit-content` | `min-w-min`, `min-w-max`, `min-w-fit` |
| `min-width: n` | `min-w-32`, `min-w-[200px]` |
| `max-width: none` | `max-w-none` |
| `max-width: 100%` | `max-w-full` |
| `max-width: 65ch` | `max-w-prose` (readable text width) |
| `max-width: 100vw` | `max-w-screen` |
| `min-height: 100vh` | `min-h-screen` |
| `min-height: 100dvh` | `min-h-dvh` |
| `min-height: 100%` | `min-h-full` |
| `min-height: 0` | `min-h-0` |
| `max-height: n` | `max-h-96`, `max-h-[400px]` |
| `max-height: 100%` | `max-h-full` |
| `max-height: 100vh` | `max-h-screen` |

**Named max-width scale (`max-w-*`)**

| Class | Width | Class | Width |
|---|---|---|---|
| `max-w-3xs` | 16rem (256px) | `max-w-3xl` | 48rem (768px) |
| `max-w-2xs` | 18rem (288px) | `max-w-4xl` | 56rem (896px) |
| `max-w-xs` | 20rem (320px) | `max-w-5xl` | 64rem (1024px) |
| `max-w-sm` | 24rem (384px) | `max-w-6xl` | 72rem (1152px) |
| `max-w-md` | 28rem (448px) | `max-w-7xl` | 80rem (1280px) |
| `max-w-lg` | 32rem (512px) | `max-w-prose` | 65ch |
| `max-w-xl` | 36rem (576px) | `max-w-full` | 100% |
| `max-w-2xl` | 42rem (672px) | `max-w-none` | none |

### 3.4 size-* (width and height together)

`size-10` sets `width` **and** `height` to 2.5rem. Perfect for avatars, icons and squares.

```html
<img class="size-10 rounded-full" />   <!-- 40x40 circle -->
<svg class="size-5" />                  <!-- 20x20 icon -->
<div class="size-full"></div>           <!-- 100% x 100% -->
<div class="size-[72px]"></div>         <!-- arbitrary -->
```

Also available: `size-px`, `size-1/2`, `size-full`, `size-auto`, `size-fit`, `size-min`, `size-max`. For the full viewport use `w-screen h-screen` (or `h-dvh`).

### 3.5 Practical Width and Height Examples

```html
<!-- Centered readable page column -->
<main class="mx-auto w-full max-w-3xl px-4">...</main>

<!-- Full-screen hero (mobile friendly) -->
<section class="min-h-dvh flex items-center justify-center">...</section>

<!-- Sidebar fixed width + flexible content -->
<div class="flex">
  <aside class="w-64 shrink-0">Sidebar</aside>
  <main class="flex-1 min-w-0">Content</main>
</div>

<!-- Scrollable list limited in height -->
<ul class="max-h-64 overflow-y-auto">...</ul>

<!-- Page height minus a 64px header -->
<div class="h-[calc(100dvh-4rem)]">...</div>

<!-- Three equal columns using fractions -->
<div class="flex"><div class="w-1/3">A</div><div class="w-1/3">B</div><div class="w-1/3">C</div></div>
```


---

## 4. Typography

### 4.1 Font Family

| Class | CSS | Use |
|---|---|---|
| `font-sans` | system sans-serif stack (UI default) | body text, UI |
| `font-serif` | system serif stack | editorial, headlines |
| `font-mono` | system monospace stack | code, numbers |
| `font-[Poppins]` | arbitrary family name | quick one-off |
| `font-(family-name:--my-font)` | from a CSS variable | v4 syntax |
| `font-display` (custom) | defined via `--font-display` in `@theme` | your own fonts |

```css
@theme { --font-display: "Poppins", sans-serif; }
```

### 4.2 Font Size (and its built-in line height)

Each `text-*` size also sets a matching `line-height`.

| Class | Font size | Line height |
|---|---|---|
| `text-xs` | 0.75rem (12px) | 1rem (16px) |
| `text-sm` | 0.875rem (14px) | 1.25rem (20px) |
| `text-base` | 1rem (16px) | 1.5rem (24px) |
| `text-lg` | 1.125rem (18px) | 1.75rem (28px) |
| `text-xl` | 1.25rem (20px) | 1.75rem (28px) |
| `text-2xl` | 1.5rem (24px) | 2rem (32px) |
| `text-3xl` | 1.875rem (30px) | 2.25rem (36px) |
| `text-4xl` | 2.25rem (36px) | 2.5rem (40px) |
| `text-5xl` | 3rem (48px) | 1 |
| `text-6xl` | 3.75rem (60px) | 1 |
| `text-7xl` | 4.5rem (72px) | 1 |
| `text-8xl` | 6rem (96px) | 1 |
| `text-9xl` | 8rem (128px) | 1 |

- **Custom size:** `text-[22px]`, `text-[1.35rem]`, `text-(length:--my-size)`.
- **Size + line height together:** `text-sm/6` (14px font, line-height 1.5rem), `text-xl/8`, `text-base/[1.7]`.

> **Heads up:** `text-` is used for both **font size** and **text color** (`text-xl` vs `text-blue-500`). Tailwind tells them apart by the value.

### 4.3 Font Weight

| Class | Weight | Class | Weight |
|---|---|---|---|
| `font-thin` | 100 | `font-semibold` | 600 |
| `font-extralight` | 200 | `font-bold` | 700 |
| `font-light` | 300 | `font-extrabold` | 800 |
| `font-normal` | 400 | `font-black` | 900 |
| `font-medium` | 500 | `font-[550]` | arbitrary (variable fonts) |

### 4.4 Font Style and Smoothing

| Class | CSS |
|---|---|
| `italic` | `font-style: italic` |
| `not-italic` | `font-style: normal` |
| `antialiased` | smoother text on macOS/iOS |
| `subpixel-antialiased` | default rendering |

### 4.5 Text Alignment

| Class | CSS |
|---|---|
| `text-left` | `text-align: left` |
| `text-center` | `text-align: center` |
| `text-right` | `text-align: right` |
| `text-justify` | `text-align: justify` |
| `text-start` | `text-align: start` (left in LTR, right in RTL) |
| `text-end` | `text-align: end` |

Vertical alignment (for inline/table-cell content): `align-baseline`, `align-top`, `align-middle`, `align-bottom`, `align-text-top`, `align-text-bottom`, `align-sub`, `align-super`.

### 4.6 Line Height (leading)

| Class | line-height | Best for |
|---|---|---|
| `leading-none` | 1 | big headings, single-line badges |
| `leading-tight` | 1.25 | headings |
| `leading-snug` | 1.375 | subheadings, short text |
| `leading-normal` | 1.5 | body text |
| `leading-relaxed` | 1.625 | long-form reading |
| `leading-loose` | 2 | very airy text |
| `leading-6` | 1.5rem | exact size from the spacing scale |
| `leading-[1.7]` | arbitrary | |

### 4.7 Letter Spacing (tracking)

| Class | letter-spacing |
|---|---|
| `tracking-tighter` | -0.05em |
| `tracking-tight` | -0.025em |
| `tracking-normal` | 0em |
| `tracking-wide` | 0.025em |
| `tracking-wider` | 0.05em |
| `tracking-widest` | 0.1em |
| `tracking-[0.2em]` | arbitrary |

Practical: `uppercase tracking-wider text-xs font-semibold` is the classic "label" style; `tracking-tight` makes big headlines look polished.

### 4.8 Text Decoration

| Class | Effect |
|---|---|
| `underline` | underline |
| `overline` | line above text |
| `line-through` | strikethrough |
| `no-underline` | removes decoration (links) |
| `decoration-solid` / `decoration-double` / `decoration-dotted` / `decoration-dashed` / `decoration-wavy` | line style |
| `decoration-blue-500` | line color |
| `decoration-1`, `decoration-2`, `decoration-4`, `decoration-auto`, `decoration-from-font` | line thickness |
| `underline-offset-1`, `-2`, `-4`, `-8`, `underline-offset-auto` | distance from text |

```html
<a class="underline decoration-wavy decoration-red-500 underline-offset-4">Error link</a>
<a class="no-underline hover:underline">Underline only on hover</a>
```

### 4.9 Text Transform

| Class | CSS |
|---|---|
| `uppercase` | `text-transform: uppercase` |
| `lowercase` | `text-transform: lowercase` |
| `capitalize` | `text-transform: capitalize` |
| `normal-case` | `text-transform: none` |

### 4.10 Text Overflow, Truncation and Line Clamp

| Class | Effect |
|---|---|
| `truncate` | one line, hides overflow, adds `...` (needs a constrained width) |
| `text-ellipsis` | `text-overflow: ellipsis` (also needs `overflow-hidden whitespace-nowrap`) |
| `text-clip` | cut off without ellipsis |
| `line-clamp-1` ... `line-clamp-6` | show N lines, then `...` |
| `line-clamp-[8]` | arbitrary line count |
| `line-clamp-none` | remove clamp (for responsive reveal) |

```html
<p class="truncate w-48">A very long single line that will be cut with an ellipsis</p>
<p class="line-clamp-3">Paragraph that shows only three lines and then adds an ellipsis...</p>

<!-- Truncate inside a flex child: min-w-0 is REQUIRED -->
<div class="flex"><span class="min-w-0 truncate">Very long name</span><button>Edit</button></div>
```

### 4.11 Whitespace

| Class | CSS | Behavior |
|---|---|---|
| `whitespace-normal` | `normal` | collapse spaces, wrap lines |
| `whitespace-nowrap` | `nowrap` | collapse spaces, never wrap |
| `whitespace-pre` | `pre` | keep spaces and newlines, never wrap |
| `whitespace-pre-line` | `pre-line` | collapse spaces, keep newlines, wrap |
| `whitespace-pre-wrap` | `pre-wrap` | keep spaces and newlines, wrap |
| `whitespace-break-spaces` | `break-spaces` | like pre-wrap, trailing spaces wrap too |

Use `whitespace-pre-line` to display multi-line text from a textarea. Use `whitespace-nowrap` for buttons and table cells that must stay on one line.

### 4.12 Word Breaking and Wrapping

| Class | Effect |
|---|---|
| `break-normal` | default behavior |
| `break-words` | break long words only if they would overflow (`overflow-wrap: break-word`) |
| `break-all` | break anywhere (URLs, hashes), can look ugly |
| `break-keep` | no breaks in CJK text |
| `wrap-break-word`, `wrap-anywhere`, `wrap-normal` | `overflow-wrap` variants (v4.1+) |
| `hyphens-none`, `hyphens-manual`, `hyphens-auto` | hyphenation (set the `lang` attribute) |
| `text-wrap`, `text-nowrap` | `text-wrap: wrap / nowrap` |
| `text-balance` | balances lines (great for headings) |
| `text-pretty` | avoids a single orphan word on the last line (great for paragraphs) |

### 4.13 More Typography Utilities

| Purpose | Classes |
|---|---|
| Indent first line | `indent-4`, `indent-8`, `-indent-4`, `indent-[2em]` |
| Numbers in tables | `tabular-nums`, `proportional-nums`, `lining-nums`, `oldstyle-nums`, `slashed-zero`, `diagonal-fractions`, `ordinal`, `normal-nums` |
| List style | see [Section 16](#16-lists) |
| Text color | `text-gray-700` ([Section 5](#5-colors)) |
| Text shadow (v4.1+) | `text-shadow-2xs`, `text-shadow-xs`, `text-shadow-sm`, `text-shadow-md`, `text-shadow-lg`, `text-shadow-none`, `text-shadow-red-500/50` |
| Text underline offset | `underline-offset-4` |
| Quotes and markers | `marker:text-blue-500`, `before:content-['']` |
| Prose styling for CMS/markdown | `prose` class from the `@tailwindcss/typography` plugin |

### 4.14 Practical Typography Recipes

```html
<!-- Page title -->
<h1 class="text-4xl md:text-6xl font-bold tracking-tight text-balance text-gray-900">
  Build faster with Tailwind
</h1>

<!-- Body paragraph -->
<p class="text-base leading-relaxed text-gray-600 max-w-prose text-pretty">...</p>

<!-- Small uppercase eyebrow label -->
<span class="text-xs font-semibold uppercase tracking-widest text-blue-600">New</span>

<!-- Muted caption -->
<small class="text-sm text-gray-500">Updated 2 days ago</small>

<!-- Price with aligned digits -->
<span class="text-2xl font-bold tabular-nums">$1,249.00</span>

<!-- Link -->
<a class="font-medium text-blue-600 underline underline-offset-4 hover:text-blue-800">Read more</a>

<!-- Monospace code chip -->
<code class="rounded bg-gray-100 px-1.5 py-0.5 font-mono text-sm text-pink-600">npm install</code>
```

---

## 5. Colors

### 5.1 The Color Scale

Tailwind ships with a large, hand-tuned palette. Each hue has **11 shades** from `50` (almost white) to `950` (almost black).

```text
50    100   200   300   400   500   600   700   800   900   950
lightest <------------------------ base (500) ----------------------> darkest
```

| Shade | Typical use |
|---|---|
| `50`, `100` | subtle backgrounds, hover tints, alert backgrounds |
| `200`, `300` | borders, dividers, disabled states |
| `400` | placeholder text, icons, dark-mode text on dark |
| `500` | the "main" brand shade, buttons, focus rings |
| `600`, `700` | hover/active button, links, body text on light |
| `800`, `900` | headings, dark UI surfaces |
| `950` | near-black surfaces, dark mode backgrounds |

**Color families:** `red`, `orange`, `amber`, `yellow`, `lime`, `green`, `emerald`, `teal`, `cyan`, `sky`, `blue`, `indigo`, `violet`, `purple`, `fuchsia`, `pink`, `rose` (vibrant) and `slate`, `gray`, `zinc`, `neutral`, `stone` (greys with different tints). v4.2 also added `mauve`, `olive`, `mist`, `taupe` (muted neutrals).

**Special values:** `black`, `white`, `transparent`, `current` (= `currentColor`), `inherit`.

> In v4 the default palette is defined in **OKLCH**, which gives more vivid colors on modern displays. You still use the same class names.

### 5.2 Color Utilities (every place a color can go)

The same pattern `{utility}-{color}-{shade}` works everywhere:

| What it colors | Prefix | Example |
|---|---|---|
| Text | `text-` | `text-blue-500` |
| Background | `bg-` | `bg-blue-500` |
| Border (all sides) | `border-` | `border-blue-500` |
| Border (one side/axis) | `border-t-`, `border-x-`... | `border-t-blue-500` |
| Ring (focus ring) | `ring-` | `ring-blue-500` |
| Ring offset gap color | `ring-offset-` | `ring-offset-white` |
| Inset ring | `inset-ring-` | `inset-ring-blue-500` |
| Divide (between children) | `divide-` | `divide-gray-200` |
| Outline | `outline-` | `outline-blue-500` |
| Box shadow | `shadow-` | `shadow-blue-500/50` |
| Inset shadow | `inset-shadow-` | `inset-shadow-blue-500` |
| Drop shadow filter | `drop-shadow-` | `drop-shadow-blue-500` |
| Text decoration | `decoration-` | `decoration-blue-500` |
| Placeholder text | `placeholder:text-` | `placeholder:text-gray-400` |
| Form accent (checkbox, radio, range) | `accent-` | `accent-blue-500` |
| Text caret (cursor) | `caret-` | `caret-blue-500` |
| SVG fill | `fill-` | `fill-blue-500` |
| SVG stroke | `stroke-` | `stroke-blue-500` |
| Gradient stops | `from-`, `via-`, `to-` | `from-blue-500` |
| Selection highlight | `selection:bg-` | `selection:bg-yellow-200` |

> **Tailwind v3 note:** v3 had `placeholder-gray-400`. In v4 use the `placeholder:` variant: `placeholder:text-gray-400`.

### 5.3 Color Opacity (the slash syntax)

Add `/` and a number from 0 to 100 to any color utility:

```html
<div class="bg-black/50"></div>        <!-- 50% black -->
<p   class="text-white/80"></p>         <!-- 80% white text -->
<div class="border-blue-500/30"></div>
<div class="bg-blue-500/[0.35]"></div>  <!-- arbitrary opacity -->
<div class="bg-blue-500/(--my-alpha)"></div> <!-- from CSS variable -->
```

> **Tailwind v3 note:** `bg-opacity-50`, `text-opacity-50`, `border-opacity-*`, `divide-opacity-*`, `ring-opacity-*` and `placeholder-opacity-*` were **removed in v4**. Use the slash syntax instead.

**Opacity of the whole element** (not just the color) is a different utility: `opacity-50` ([Section 8](#8-shadows--effects)).

### 5.4 Special Color Keywords

| Class | CSS value | Use |
|---|---|---|
| `bg-transparent` | transparent | clear background |
| `text-current` / `border-current` | `currentColor` | inherit the text color (icons) |
| `bg-inherit`, `text-inherit` | `inherit` | take parent's value |
| `text-black`, `text-white`, `bg-black`, `bg-white` | fixed | |

```html
<button class="text-blue-600 hover:text-blue-800">
  <svg class="size-5 fill-current">...</svg> Save   <!-- icon follows text color -->
</button>
```

### 5.5 Arbitrary Colors

| Format | Example |
|---|---|
| Hex | `bg-[#1e293b]`, `text-[#f43f5e]` |
| Hex + alpha | `bg-[#1e293b80]` |
| RGB | `text-[rgb(20,30,40)]`, `bg-[rgb(20_30_40/0.5)]` |
| HSL | `bg-[hsl(210,40%,96%)]` |
| OKLCH | `bg-[oklch(0.7_0.15_200)]` |
| CSS variable | `bg-(--brand)` (v4) or `bg-[var(--brand)]` |
| With type hint | `text-(color:--my-color)`, `text-[color:var(--c)]` |

Use `_` for spaces inside the brackets. When the value is ambiguous (for example `text-[var(--x)]` could be a size or a color) add a type hint: `text-[color:var(--x)]` or `text-[length:var(--x)]`.

### 5.6 Defining Your Own Colors (v4)

```css
@import "tailwindcss";
@theme {
  --color-brand-50:  oklch(0.97 0.02 260);
  --color-brand-500: oklch(0.62 0.2 260);
  --color-brand-900: oklch(0.3 0.1 260);
}
```

This instantly creates `bg-brand-500`, `text-brand-900`, `border-brand-50`, `ring-brand-500/40` and so on.

### 5.7 Color Mixing Examples

```html
<div class="bg-blue-500/10 text-blue-700 border border-blue-500/30 rounded-lg p-4">Info alert</div>
<div class="bg-white/60 backdrop-blur-md border border-white/40">Glass panel</div>
<button class="bg-blue-600 hover:bg-blue-700 active:bg-blue-800 text-white">Button</button>
<input class="border-gray-300 focus:border-blue-500 focus:ring-blue-500/30 caret-blue-500 accent-blue-500" />
```

---

## 6. Backgrounds

### 6.1 Background Color

`bg-{color}-{shade}`, `bg-white`, `bg-black`, `bg-transparent`, `bg-current`, `bg-inherit`, `bg-black/50`, `bg-[#hex]`.

### 6.2 Background Image

| Class | CSS |
|---|---|
| `bg-none` | `background-image: none` |
| `bg-[url(/img/hero.jpg)]` | image from a URL (arbitrary value) |
| `bg-[url('/img/my_hero.jpg')]` | quote paths with special characters |
| `bg-(image:--hero)` | from a CSS variable |

```html
<section class="bg-[url(/hero.jpg)] bg-cover bg-center bg-no-repeat min-h-96"></section>
```

> In React with a bundler, import the image and use inline `style={{ backgroundImage: `url(${hero})` }}` for dynamic images (Tailwind cannot see dynamic URLs).

### 6.3 Background Size

| Class | CSS |
|---|---|
| `bg-auto` | original size |
| `bg-cover` | fill the area, crop if needed (most common) |
| `bg-contain` | fit inside, no crop |
| `bg-size-[200px_100px]` | arbitrary size |

### 6.4 Background Position

`bg-center`, `bg-top`, `bg-bottom`, `bg-left`, `bg-right`, `bg-left-top`, `bg-left-bottom`, `bg-right-top`, `bg-right-bottom`, `bg-position-[center_top_1rem]` (arbitrary).

### 6.5 Background Repeat

`bg-repeat`, `bg-no-repeat`, `bg-repeat-x`, `bg-repeat-y`, `bg-repeat-round`, `bg-repeat-space`.

### 6.6 Background Attachment

| Class | Effect |
|---|---|
| `bg-fixed` | stays fixed while page scrolls (parallax look) |
| `bg-local` | scrolls with the element's content |
| `bg-scroll` | scrolls with the page (default) |

### 6.7 Background Clip and Origin

| Class | CSS |
|---|---|
| `bg-clip-border` | background extends under the border (default) |
| `bg-clip-padding` | background stops at the border |
| `bg-clip-content` | background only behind content |
| `bg-clip-text` | background shows only inside the text shapes (gradient text) |
| `bg-origin-border` | positioning area starts at the border box |
| `bg-origin-padding` | starts at the padding box (default) |
| `bg-origin-content` | starts at the content box |

### 6.8 Gradients

**Linear gradients (v4: `bg-linear-*`)**

| Class | Direction |
|---|---|
| `bg-linear-to-t` | to top |
| `bg-linear-to-tr` | to top right |
| `bg-linear-to-r` | to right |
| `bg-linear-to-br` | to bottom right |
| `bg-linear-to-b` | to bottom |
| `bg-linear-to-bl` | to bottom left |
| `bg-linear-to-l` | to left |
| `bg-linear-to-tl` | to top left |
| `bg-linear-45` | exact angle (any number; negative with `-bg-linear-45`) |
| `bg-linear-[25deg,red_5%,yellow_60%,lime_90%]` | fully custom |

**Other gradient types (v4)**

| Class | Gradient |
|---|---|
| `bg-radial` | radial (circle from center) |
| `bg-radial-[at_25%_25%]` | radial with a custom position |
| `bg-conic` | conic (color wheel) |
| `bg-conic-180` | conic starting at an angle |

**Color stops:** `from-{color}`, `via-{color}`, `to-{color}`, and optional positions: `from-10%`, `via-30%`, `to-90%`.

**Color space (v4):** add an interpolation modifier for smoother or different blends: `bg-linear-to-r/oklch`, `bg-linear-to-r/srgb`, `bg-linear-to-r/hsl`, `bg-linear-to-r/longer`.

```html
<!-- Simple two-color gradient -->
<div class="bg-linear-to-r from-indigo-500 to-purple-600 p-8 text-white rounded-xl"></div>

<!-- Three stops -->
<div class="bg-linear-to-br from-pink-500 via-red-500 to-yellow-500"></div>

<!-- Fade to transparent over an image (card overlay) -->
<div class="absolute inset-0 bg-linear-to-t from-black/70 to-transparent"></div>

<!-- Gradient text -->
<h1 class="bg-linear-to-r from-blue-500 to-fuchsia-500 bg-clip-text text-transparent text-5xl font-extrabold">
  Gradient Heading
</h1>

<!-- Radial spotlight -->
<div class="bg-radial from-white to-slate-200"></div>
```

> **Tailwind v3 note:** v3 used `bg-gradient-to-r`. In v4 the preferred name is `bg-linear-to-r`; the old `bg-gradient-to-*` names still work as legacy aliases, but use the new names in new code.

### 6.9 Practical Background Recipes

```html
<!-- Hero with image + dark overlay -->
<section class="relative isolate min-h-dvh bg-[url(/hero.jpg)] bg-cover bg-center">
  <div class="absolute inset-0 -z-10 bg-black/50"></div>
  <div class="mx-auto max-w-3xl px-4 py-32 text-white">...</div>
</section>

<!-- Dotted pattern with arbitrary background -->
<div class="bg-[radial-gradient(#cbd5e1_1px,transparent_1px)] bg-size-[16px_16px]"></div>

<!-- Subtle page background -->
<body class="bg-gray-50 text-gray-900 dark:bg-gray-950 dark:text-gray-100">
```


---

## 7. Borders & Radius

### 7.1 Border Width

| Class | CSS |
|---|---|
| `border` | `border-width: 1px` (all sides) |
| `border-0` | 0 |
| `border-2` | 2px |
| `border-4` | 4px |
| `border-8` | 8px |
| `border-[3px]` | arbitrary |
| `border-x`, `border-y` | left+right / top+bottom (1px); also `border-x-2`, `border-y-4` |
| `border-t`, `border-r`, `border-b`, `border-l` | one side (1px); also `border-t-2`, `border-b-4`... |
| `border-s`, `border-e` | inline start / end (RTL aware) |

> **Important (v4):** the default border color is now `currentColor`, not light gray. **Always pair `border` with a color**: `border border-gray-200`.

### 7.2 Border Color and Opacity

`border-{color}-{shade}`, `border-transparent`, `border-current`, side-specific `border-t-red-500`, `border-x-gray-200`, opacity with `border-blue-500/30`.

> **Tailwind v3 note:** `border-opacity-*` is removed in v4. Use `border-black/20`.

### 7.3 Border Style

`border-solid`, `border-dashed`, `border-dotted`, `border-double`, `border-hidden`, `border-none`.

```html
<div class="border-2 border-dashed border-gray-300 rounded-lg p-8 text-center">Drop files here</div>
```

### 7.4 Divide (borders between children)

| Class | Effect |
|---|---|
| `divide-x` / `divide-x-2` / `divide-x-4` | vertical lines between horizontally placed children |
| `divide-y` / `divide-y-2` | horizontal lines between stacked children |
| `divide-gray-200` | color of the dividers |
| `divide-dashed`, `divide-dotted`, `divide-solid`, `divide-double`, `divide-none` | style |
| `divide-x-reverse`, `divide-y-reverse` | for reversed flex directions |

```html
<ul class="divide-y divide-gray-200">
  <li class="py-3">Item one</li>
  <li class="py-3">Item two</li>
  <li class="py-3">Item three</li>
</ul>
```

### 7.5 Outline and Ring

| Class | Effect |
|---|---|
| `outline` / `outline-1` / `outline-2` / `outline-4` / `outline-8` | outline width |
| `outline-blue-500` | color |
| `outline-offset-2` / `-4` / `-8` / `-0` | gap between element and outline |
| `outline-dashed`, `outline-dotted`, `outline-double`, `outline-solid` | style |
| `outline-hidden` | removes the default outline but keeps it visible in forced-colors mode (accessible reset) |
| `outline-none` | `outline-style: none` (v4: really removes it, avoid on focusable elements) |
| `ring` | 1px ring (box-shadow based, follows border-radius) |
| `ring-0`, `ring-1`, `ring-2`, `ring-3`, `ring-4`, `ring-8` | ring width |
| `ring-blue-500`, `ring-blue-500/50` | ring color |
| `ring-offset-2`, `ring-offset-white` | gap + gap color between element and ring |
| `inset-ring`, `inset-ring-2`, `inset-ring-blue-500` | ring drawn inside the element |

```html
<button class="outline-hidden focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2">Accessible</button>
```

> **Tailwind v3 note:** v3 `ring` was 3px blue. In v4 `ring` is 1px and `currentColor`; write `ring-3 ring-blue-500` to get the old look. v3 `outline-none` became `outline-hidden`.

### 7.6 Border Radius

| Class | Radius | Pixels |
|---|---|---|
| `rounded-none` | 0 | 0 |
| `rounded-xs` | 0.125rem | 2px |
| `rounded-sm` | 0.25rem | 4px |
| `rounded-md` | 0.375rem | 6px |
| `rounded-lg` | 0.5rem | 8px |
| `rounded-xl` | 0.75rem | 12px |
| `rounded-2xl` | 1rem | 16px |
| `rounded-3xl` | 1.5rem | 24px |
| `rounded-4xl` | 2rem | 32px |
| `rounded-full` | 9999px | pill or circle |
| `rounded-[10px]` | arbitrary | |

> **Tailwind v3 note:** v3 had bare `rounded` (4px) and `rounded-sm` (2px). In v4 those are `rounded-sm` (4px) and `rounded-xs` (2px). Use the sized names.

### 7.7 Individual Corners and Sides

| Target | Class prefix | Example |
|---|---|---|
| top (both top corners) | `rounded-t-*` | `rounded-t-lg` |
| right | `rounded-r-*` | `rounded-r-lg` |
| bottom | `rounded-b-*` | `rounded-b-lg` |
| left | `rounded-l-*` | `rounded-l-lg` |
| top-left | `rounded-tl-*` | `rounded-tl-2xl` |
| top-right | `rounded-tr-*` | `rounded-tr-2xl` |
| bottom-right | `rounded-br-*` | `rounded-br-2xl` |
| bottom-left | `rounded-bl-*` | `rounded-bl-2xl` |
| logical start / end | `rounded-s-*`, `rounded-e-*` | `rounded-s-lg` |
| logical corners | `rounded-ss-*`, `rounded-se-*`, `rounded-es-*`, `rounded-ee-*` | `rounded-ss-xl` |

```html
<img class="size-24 rounded-full object-cover" />                  <!-- circle avatar -->
<button class="rounded-full px-6 py-2">Pill button</button>
<div class="rounded-t-xl border border-b-0">Tab header</div>
<div class="rounded-tl-3xl rounded-br-3xl bg-blue-500 p-6">Leaf shape</div>
```

---

## 8. Shadows & Effects

### 8.1 Box Shadow

| Class | Look | Use |
|---|---|---|
| `shadow-2xs` | barely there | hairline lift |
| `shadow-xs` | very subtle | inputs |
| `shadow-sm` | small | cards, buttons |
| `shadow-md` | medium | raised cards |
| `shadow-lg` | large | dropdowns, hover state |
| `shadow-xl` | extra large | modals |
| `shadow-2xl` | huge | hero images, floating panels |
| `shadow-none` | removes shadow | reset (for example on hover or breakpoint) |
| `shadow-[0_4px_20px_rgba(0,0,0,0.15)]` | custom | exact design match |
| `shadow-blue-500/50` | colored shadow | glow effects |

**Inset shadows and rings (v4):** `inset-shadow-2xs`, `inset-shadow-xs`, `inset-shadow-sm`, `inset-shadow-none`, `inset-shadow-black/20`, `inset-ring-1`.

```html
<div class="rounded-xl bg-white shadow-md hover:shadow-xl transition-shadow">Card</div>
<button class="bg-blue-500 text-white shadow-lg shadow-blue-500/40">Glowing button</button>
<div class="inset-shadow-sm bg-gray-100 rounded-lg p-4">Pressed look</div>
```

> **Tailwind v3 note:** the scale shifted down one step: v3 `shadow-sm` is v4 `shadow-xs`; v3 `shadow` is v4 `shadow-sm`. v3 `shadow-inner` is replaced by `inset-shadow-*`. v3 `drop-shadow` follows the same rename (see [Section 22](#22-filters--visual-effects)).

**Custom shadow tokens**

```css
@theme { --shadow-soft: 0 8px 30px rgb(0 0 0 / 0.12); }  /* creates shadow-soft */
```

### 8.2 Opacity

`opacity-0`, `opacity-5`, `opacity-10`, `opacity-15`, `opacity-20`, `opacity-25`, `opacity-30` ... `opacity-95`, `opacity-100`, `opacity-[0.37]`.

`opacity-*` fades the **whole element including its children**. To fade only the background, use `bg-black/50`.

### 8.3 Blend Modes

| Utility | Classes |
|---|---|
| `mix-blend-*` (element blends with what is behind) | `mix-blend-normal`, `multiply`, `screen`, `overlay`, `darken`, `lighten`, `color-dodge`, `color-burn`, `hard-light`, `soft-light`, `difference`, `exclusion`, `hue`, `saturation`, `color`, `luminosity`, `plus-darker`, `plus-lighter` |
| `bg-blend-*` (background layers blend) | `bg-blend-normal`, `multiply`, `screen`, `overlay`, `darken`, `lighten`, `color-dodge`, `color-burn`, `hard-light`, `soft-light`, `difference`, `exclusion`, `hue`, `saturation`, `color`, `luminosity` |

```html
<div class="bg-blue-500 bg-[url(/photo.jpg)] bg-blend-multiply bg-cover">Tinted photo</div>
<img class="mix-blend-multiply" />   <!-- logo that blends into a colored background -->
```

### 8.4 Box Decoration Break

`box-decoration-clone` / `box-decoration-slice`: controls how backgrounds, borders and padding render when an inline element wraps across lines (highlighted text).

```html
<span class="box-decoration-clone bg-yellow-200 px-2 leading-loose">A highlighted phrase that wraps over multiple lines</span>
```

> **Tailwind v3 note:** v3 names were `decoration-clone` / `decoration-slice`.

### 8.5 Isolation (stacking contexts)

| Class | Effect |
|---|---|
| `isolate` | creates a new stacking context (z-index children stay inside) |
| `isolation-auto` | default |

Use `isolate` on a card so a child with `-z-10` (overlays) does not slip behind the page background.

### 8.6 Masks (v4.1+)

Mask utilities fade or cut parts of an element using a gradient or image as an alpha mask. Common ones: `mask-t-from-50%` (fade the top edge), `mask-b-from-50%` (fade the bottom edge), `mask-radial-from-50%` (radial fade), `mask-[url(/shape.svg)]` (custom shape). Example: fade the bottom of a scroll area with `mask-b-from-80%`. See the Tailwind docs (Masks) for the full list.

---

## 9. Flexbox

### 9.1 The Mental Model: Main Axis and Cross Axis

Flexbox places children along a **main axis**. The **cross axis** is perpendicular.

- `justify-*` aligns along the **main axis**
- `items-*` aligns along the **cross axis**

```text
flex-row (default)                         flex-col
main axis  ------------------>             main axis (vertical)
                                           |
 +---------------------------------+       |   +---------------+
 |  [A]   [B]   [C]                |  ^    |   |  [A]          |
 |                                 |  |    v   |  [B]          |
 +---------------------------------+  |        |  [C]          |
 cross axis (vertical) <--------------+        +---------------+
                                               cross axis ------>
 justify-* = left/right placement              justify-* = top/bottom placement
 items-*   = top/bottom placement              items-*   = left/right placement
```

**Remember:** when you switch to `flex-col`, `justify` and `items` swap their visual direction.

### 9.2 Flex Container

| Class | CSS |
|---|---|
| `flex` | `display: flex` (block-level) |
| `inline-flex` | `display: inline-flex` |
| `flex-row` | `flex-direction: row` (default) |
| `flex-row-reverse` | reverse order horizontally |
| `flex-col` | `flex-direction: column` |
| `flex-col-reverse` | reverse order vertically |
| `flex-wrap` | allow wrapping to new lines |
| `flex-nowrap` | never wrap (default) |
| `flex-wrap-reverse` | wrap upwards |
| `gap-4`, `gap-x-4`, `gap-y-2` | space between items |

### 9.3 Justify Content (main axis)

| Class | Result |
|---|---|
| `justify-start` | items at the start |
| `justify-center` | items in the center |
| `justify-end` | items at the end |
| `justify-between` | first at start, last at end, equal space between |
| `justify-around` | equal space around each item (half-space at edges) |
| `justify-evenly` | equal space everywhere including edges |
| `justify-stretch` | stretch auto-sized items to fill |
| `justify-normal` | default |

```text
justify-start    [A][B][C]·················
justify-center   ·········[A][B][C]·········
justify-end      ·················[A][B][C]
justify-between  [A]·········[B]·········[C]
justify-around   ··[A]······[B]······[C]··
justify-evenly   ···[A]·····[B]·····[C]···
```

### 9.4 Align Items (cross axis)

| Class | Result |
|---|---|
| `items-start` | align to the top (in a row) |
| `items-center` | center vertically (in a row) |
| `items-end` | align to the bottom |
| `items-baseline` | align text baselines (mixed font sizes) |
| `items-stretch` | stretch to container height (default) |

```text
items-start      items-center     items-end        items-stretch
+----------+     +----------+     +----------+     +----------+
|[A][B][C] |     |          |     |          |     |[A][B][C] |
|          |     |[A][B][C] |     |          |     |[ ][ ][ ] |
|          |     |          |     |[A][B][C] |     |[ ][ ][ ] |
+----------+     +----------+     +----------+     +----------+
```

### 9.5 Align Content (multi-line flex only)

`content-start`, `content-center`, `content-end`, `content-between`, `content-around`, `content-evenly`, `content-stretch`, `content-normal`. These only matter when `flex-wrap` produces **multiple rows** and the container is taller than the rows.

### 9.6 Align Self (one item overrides `items-*`)

`self-auto`, `self-start`, `self-center`, `self-end`, `self-stretch`, `self-baseline`.

Also: `justify-self-*` and `justify-items-*` are for **grid**, see [Section 10](#10-css-grid).

### 9.7 Flex Item Sizing: flex, grow, shrink, basis

| Class | CSS | Meaning |
|---|---|---|
| `flex-1` | `flex: 1 1 0%` | grow and shrink, start from 0 (equal-width columns) |
| `flex-auto` | `flex: 1 1 auto` | grow and shrink from content size |
| `flex-initial` | `flex: 0 1 auto` | shrink only, never grow |
| `flex-none` | `flex: none` | fixed, does not grow or shrink |
| `flex-[2]` | `flex: 2` | grow factor 2 (arbitrary) |
| `grow` / `grow-0` | `flex-grow: 1 / 0` | take up leftover space or not |
| `grow-[3]` | arbitrary | |
| `shrink` / `shrink-0` | `flex-shrink: 1 / 0` | allowed to shrink or not |
| `basis-1/2`, `basis-1/3`, `basis-full`, `basis-auto` | `flex-basis` | initial size before grow/shrink |
| `basis-64`, `basis-[200px]` | | |
| `order-1`...`order-12`, `order-first`, `order-last`, `order-none` | `order` | change visual order |

> **Tailwind v3 note:** v3 also had `flex-grow` and `flex-shrink` (and `flex-grow-0`, `flex-shrink-0`). In v4 write `grow`, `shrink`, `grow-0`, `shrink-0`.

### 9.8 Practical Flexbox Recipes

```html
<!-- Center anything (horizontally + vertically) -->
<div class="flex items-center justify-center h-64">Centered</div>

<!-- Navbar: logo left, links right -->
<nav class="flex items-center justify-between px-6 py-4">
  <a class="font-bold">Logo</a>
  <ul class="flex items-center gap-6"><li>Home</li><li>About</li></ul>
</nav>

<!-- Vertical stack with gap -->
<div class="flex flex-col gap-4">...</div>

<!-- Sidebar + content -->
<div class="flex min-h-screen">
  <aside class="w-64 shrink-0 bg-gray-900 text-white">Sidebar</aside>
  <main class="flex-1 min-w-0 p-6">Content</main>
</div>

<!-- Sticky footer: footer sits at the bottom even with little content -->
<div class="flex min-h-screen flex-col">
  <header>...</header>
  <main class="flex-1">...</main>
  <footer>...</footer>
</div>

<!-- Wrapping tag list -->
<div class="flex flex-wrap gap-2"><span class="rounded-full bg-gray-100 px-3 py-1 text-sm">Tag</span></div>

<!-- Row on desktop, column on mobile -->
<div class="flex flex-col md:flex-row gap-6">...</div>

<!-- Push last item right -->
<div class="flex items-center gap-3"><h2>Title</h2><button class="ml-auto">Action</button></div>

<!-- Icon + text button -->
<button class="inline-flex items-center gap-2 rounded-lg bg-blue-500 px-4 py-2 text-white">
  <svg class="size-4">...</svg> Save
</button>
```

---

## 10. CSS Grid

### 10.1 Grid Container

| Class | CSS |
|---|---|
| `grid` | `display: grid` |
| `inline-grid` | `display: inline-grid` |
| `grid-cols-1` ... `grid-cols-12` | `grid-template-columns: repeat(n, minmax(0, 1fr))` |
| `grid-cols-none` | none |
| `grid-cols-subgrid` | inherit parent's column tracks |
| `grid-cols-[200px_1fr]` | custom track list (arbitrary) |
| `grid-cols-[repeat(auto-fit,minmax(250px,1fr))]` | auto-responsive columns |
| `grid-rows-1` ... `grid-rows-12`, `grid-rows-none`, `grid-rows-subgrid`, `grid-rows-[auto_1fr_auto]` | rows |
| `gap-4`, `gap-x-4`, `gap-y-4` | spacing between cells |

In v4 any number is accepted (`grid-cols-13`).

### 10.2 Grid Items: Spanning and Placement

| Class | CSS |
|---|---|
| `col-span-1` ... `col-span-12` | span N columns |
| `col-span-full` | `grid-column: 1 / -1` |
| `col-auto` | auto placement |
| `col-start-1` ... `col-start-13`, `col-start-auto` | start line |
| `col-end-1` ... `col-end-13`, `col-end-auto` | end line |
| `col-[2/span_3]` | arbitrary |
| `row-span-1` ... `row-span-12`, `row-span-full` | span rows |
| `row-start-*`, `row-end-*`, `row-auto` | row lines |

```html
<div class="grid grid-cols-4 gap-4">
  <div class="col-span-2">Wide</div>
  <div>Normal</div>
  <div class="row-span-2">Tall</div>
  <div class="col-start-2 col-end-4">Placed between lines 2 and 4</div>
</div>
```

### 10.3 Auto Flow and Auto Tracks

| Class | Effect |
|---|---|
| `grid-flow-row` | fill row by row (default) |
| `grid-flow-col` | fill column by column |
| `grid-flow-dense` | backfill holes |
| `grid-flow-row-dense`, `grid-flow-col-dense` | combined |
| `auto-cols-auto`, `auto-cols-min`, `auto-cols-max`, `auto-cols-fr` | size of implicit columns |
| `auto-rows-auto`, `auto-rows-min`, `auto-rows-max`, `auto-rows-fr` | size of implicit rows |
| `auto-rows-[minmax(100px,auto)]` | arbitrary |

### 10.4 Alignment in Grid

| Class | Applies to | CSS |
|---|---|---|
| `justify-items-start / center / end / stretch` | all items (inline axis) | `justify-items` |
| `justify-self-auto / start / center / end / stretch` | one item | `justify-self` |
| `items-start / center / end / stretch / baseline` | all items (block axis) | `align-items` |
| `self-start / center / end / stretch` | one item | `align-self` |
| `justify-start / center / end / between / around / evenly` | the whole grid | `justify-content` |
| `content-start / center / end / between / around / evenly` | the whole grid | `align-content` |
| `place-items-start / center / end / stretch / baseline` | both axes at once | `place-items` |
| `place-content-start / center / end / between / around / evenly / stretch` | both axes, whole grid | `place-content` |
| `place-self-auto / start / center / end / stretch` | one item, both axes | `place-self` |

`place-items-center` is the shortest way to center content in a grid cell: `grid place-items-center min-h-screen`.

### 10.5 Practical Grid Layouts

```html
<!-- Responsive card grid: 1 / 2 / 3 / 4 columns -->
<div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
  <div class="rounded-xl border border-gray-200 bg-white p-6 shadow-sm">Card</div>
  <!-- repeat -->
</div>

<!-- Auto-fit cards: as many 250px+ columns as fit, no breakpoints needed -->
<div class="grid grid-cols-[repeat(auto-fit,minmax(250px,1fr))] gap-6">...</div>

<!-- Sidebar layout: fixed 240px + flexible content -->
<div class="grid grid-cols-[240px_1fr] min-h-screen">
  <aside>Sidebar</aside><main>Content</main>
</div>

<!-- Holy grail layout -->
<div class="grid min-h-screen grid-rows-[auto_1fr_auto] grid-cols-[200px_1fr]">
  <header class="col-span-2">Header</header>
  <nav>Nav</nav>
  <main>Main</main>
  <footer class="col-span-2">Footer</footer>
</div>

<!-- Dashboard: big featured card + small cards -->
<div class="grid grid-cols-3 grid-rows-2 gap-4">
  <div class="col-span-2 row-span-2">Chart</div>
  <div>Stat 1</div>
  <div>Stat 2</div>
</div>

<!-- Perfectly centered page -->
<div class="grid min-h-screen place-items-center">Centered</div>
```

**Flex vs Grid:** use **flex** for one-dimensional rows or columns (navbars, button groups). Use **grid** when you control rows **and** columns (page layouts, card galleries).


---

## 11. Positioning

### 11.1 Position Types

| Class | CSS | Behavior |
|---|---|---|
| `static` | `position: static` | normal flow (default), `top/left/z-index` ignored |
| `relative` | `position: relative` | normal flow, but can be nudged and becomes the **anchor** for `absolute` children |
| `absolute` | `position: absolute` | removed from flow, placed relative to the nearest positioned ancestor |
| `fixed` | `position: fixed` | placed relative to the viewport, stays while scrolling |
| `sticky` | `position: sticky` | scrolls normally until it hits a threshold (`top-0`), then sticks |

**Golden rule:** put `relative` on the parent whenever a child uses `absolute`.

### 11.2 Inset (top, right, bottom, left)

| Class | CSS |
|---|---|
| `inset-0` | `top, right, bottom, left: 0` (cover the parent) |
| `inset-x-0` | `left: 0; right: 0` |
| `inset-y-0` | `top: 0; bottom: 0` |
| `top-0`, `right-0`, `bottom-0`, `left-0` | one side |
| `start-0`, `end-0` | logical left/right (RTL aware) |
| `top-4`, `right-2`, `-top-2`, `-left-1` | spacing scale and negatives |
| `top-1/2`, `left-1/2`, `inset-x-1/4` | fractions (percent) |
| `top-full`, `bottom-full` | 100% (place outside the edge) |
| `top-[10px]`, `inset-[5px]` | arbitrary |
| `inset-auto`, `top-auto` | auto |

### 11.3 Z-Index

`z-0`, `z-10`, `z-20`, `z-30`, `z-40`, `z-50`, `z-auto`, `-z-10`, `z-[100]`. In v4 any integer works: `z-60`.

Suggested layering convention: content `z-0`, sticky header `z-10`, dropdown `z-20`, overlay `z-30`, modal `z-40`/`z-50`, toast `z-50`.

### 11.4 Positioning Recipes

```html
<!-- Badge in the corner of a card -->
<div class="relative rounded-xl border p-6">
  <span class="absolute top-0 right-0 -mt-2 -mr-2 rounded-full bg-red-500 px-2 py-0.5 text-xs text-white">New</span>
</div>

<!-- Cover the parent (overlay) -->
<div class="relative">
  <img class="w-full" />
  <div class="absolute inset-0 bg-black/40"></div>
</div>

<!-- Perfectly centered absolute element -->
<div class="absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2">Centered</div>

<!-- Floating action button -->
<button class="fixed bottom-4 right-4 size-14 rounded-full bg-blue-600 text-white shadow-lg">+</button>

<!-- Sticky header -->
<header class="sticky top-0 z-10 bg-white/80 backdrop-blur border-b">...</header>

<!-- Fixed full-screen modal backdrop -->
<div class="fixed inset-0 z-50 bg-black/50"></div>

<!-- Input with icon inside -->
<div class="relative">
  <svg class="absolute left-3 top-1/2 size-5 -translate-y-1/2 text-gray-400">...</svg>
  <input class="w-full rounded-lg border py-2 pl-10 pr-3" />
</div>

<!-- Dropdown menu below a button -->
<div class="relative">
  <button>Menu</button>
  <div class="absolute right-0 top-full mt-2 w-48 rounded-lg bg-white shadow-lg">...</div>
</div>
```

> **Sticky not working?** The parent (or any ancestor) must not have `overflow-hidden`/`overflow-auto`, and you must set a threshold such as `top-0`.

---

## 12. Display

| Class | CSS | When to use |
|---|---|---|
| `block` | `display: block` | full-width block; stack vertically; make `<a>` or `<span>` behave like a box |
| `inline-block` | `display: inline-block` | sits in a text line but accepts width, height, margin |
| `inline` | `display: inline` | flows with text; ignores width/height and vertical margin |
| `flex` | `display: flex` | one-dimensional layouts (rows/columns) |
| `inline-flex` | `display: inline-flex` | flex container that sits inline (buttons with icons, badges) |
| `grid` | `display: grid` | two-dimensional layouts |
| `inline-grid` | `display: inline-grid` | inline grid container |
| `table`, `table-row`, `table-cell`, `table-caption`, `table-column`, `table-column-group`, `table-header-group`, `table-footer-group`, `table-row-group`, `inline-table` | table display values | build table-like layouts without `<table>` |
| `flow-root` | `display: flow-root` | contain floats / prevent margin collapse |
| `contents` | `display: contents` | the element's box disappears; its children behave as children of the parent |
| `list-item` | `display: list-item` | make an element behave like an `<li>` |
| `hidden` | `display: none` | **removes from layout** and from the accessibility tree |
| `invisible` / `visible` | `visibility` | hidden but **still takes up space** |
| `sr-only` | visually hidden | still read by screen readers ([Section 30](#30-accessibility)) |

```html
<!-- Show on desktop only / mobile only -->
<nav class="hidden md:flex">Desktop menu</nav>
<button class="md:hidden">Hamburger</button>

<!-- Link that fills its container (large click area) -->
<a class="block px-4 py-2 hover:bg-gray-100">Menu item</a>

<!-- Toggle visibility without layout shift -->
<div class="invisible group-hover:visible">Tooltip</div>
```

**Other layout helpers:** `float-left`, `float-right`, `float-none`, `clear-both`, `box-border` (default in Tailwind), `box-content`, `columns-2`, `columns-3`, `columns-xs`, `break-inside-avoid` (masonry-style columns).

---

## 13. Overflow

| Class | CSS | Behavior |
|---|---|---|
| `overflow-auto` | `overflow: auto` | scrollbars only when content overflows |
| `overflow-hidden` | `overflow: hidden` | clip overflowing content, no scrollbar (also rounds image corners, clears floats) |
| `overflow-clip` | `overflow: clip` | clip, no scroll container created |
| `overflow-visible` | `overflow: visible` | content spills out (default) |
| `overflow-scroll` | `overflow: scroll` | always show scrollbars |
| `overflow-x-auto`, `overflow-x-hidden`, `overflow-x-scroll`, `overflow-x-clip`, `overflow-x-visible` | horizontal only | |
| `overflow-y-auto`, `overflow-y-hidden`, `overflow-y-scroll`, `overflow-y-clip`, `overflow-y-visible` | vertical only | |
| `overscroll-auto`, `overscroll-contain`, `overscroll-none` | scroll chaining | stop a modal from scrolling the page behind it |
| `overscroll-x-contain`, `overscroll-y-none` | per axis | |

```html
<!-- Scrollable table wrapper on small screens -->
<div class="overflow-x-auto"><table class="min-w-full">...</table></div>

<!-- Rounded card that clips its image -->
<div class="overflow-hidden rounded-xl"><img class="w-full" /></div>

<!-- Scroll area -->
<div class="h-64 overflow-y-auto">...</div>

<!-- Horizontal scrolling row with snap -->
<div class="flex snap-x snap-mandatory gap-4 overflow-x-auto">
  <div class="w-64 shrink-0 snap-start">1</div>
  <div class="w-64 shrink-0 snap-start">2</div>
</div>
```

---

## 14. Object & Image Utilities

`object-*` controls how **replaced elements** (`<img>`, `<video>`) fit inside their box. It needs a set width and height.

### 14.1 Object Fit

| Class | Behavior |
|---|---|
| `object-contain` | whole image visible, keeps ratio, may leave empty space |
| `object-cover` | fills the box, keeps ratio, crops the excess (most used) |
| `object-fill` | stretches (distorts) to fill |
| `object-none` | original size, not resized |
| `object-scale-down` | `none` or `contain`, whichever is smaller |

### 14.2 Object Position

`object-center`, `object-top`, `object-bottom`, `object-left`, `object-right`, `object-left-top`, `object-left-bottom`, `object-right-top`, `object-right-bottom`, `object-[25%_75%]`.

### 14.3 Image Examples

```html
<!-- Circular avatar -->
<img class="size-16 rounded-full object-cover" src="..." alt="User" />

<!-- Card image with fixed height, cropped nicely -->
<img class="h-48 w-full object-cover object-top" src="..." alt="" />

<!-- Responsive image -->
<img class="max-w-full h-auto" src="..." alt="" />

<!-- Logo that must never be cropped -->
<img class="h-10 w-auto object-contain" src="..." alt="Logo" />

<!-- Video background -->
<video class="absolute inset-0 -z-10 h-full w-full object-cover" autoplay muted loop></video>

<!-- Grayscale photo that becomes colored on hover -->
<img class="grayscale hover:grayscale-0 transition duration-300" src="..." alt="" />
```

---

## 15. Aspect Ratio

| Class | CSS |
|---|---|
| `aspect-auto` | natural ratio |
| `aspect-square` | `1 / 1` |
| `aspect-video` | `16 / 9` |
| `aspect-4/3`, `aspect-3/2`, `aspect-2/1`... | any `a/b` ratio (v4 shorthand) |
| `aspect-[4/3]`, `aspect-[21/9]` | arbitrary ratio |

```html
<div class="aspect-video w-full overflow-hidden rounded-xl bg-gray-200">
  <iframe class="size-full" src="https://www.youtube.com/embed/..."></iframe>
</div>

<img class="aspect-square w-full rounded-lg object-cover" src="..." alt="" />   <!-- perfect square thumbnail -->
<div class="aspect-[3/4] w-48 bg-gray-100">Portrait placeholder</div>
```

Use aspect ratio with **one dimension set** (usually width) so the other is computed. Pair with `object-cover` for images.

---

## 16. Lists

| Class | Effect |
|---|---|
| `list-none` | no bullets or numbers (also remove default padding yourself) |
| `list-disc` | bullets |
| `list-decimal` | 1. 2. 3. |
| `list-inside` | marker inside the content box (text wraps under the marker) |
| `list-outside` | marker outside (default) |
| `list-image-[url(/dot.svg)]` | custom marker image |
| `list-[upper-roman]`, `list-[lower-alpha]` | any CSS `list-style-type` (arbitrary) |
| `marker:text-blue-500` | style the marker with the `marker:` variant |

> Tailwind's reset removes list styling. You **must** add `list-disc` or `list-decimal` to see bullets or numbers, and usually `pl-5` (or `list-inside`) for indentation.

```html
<ul class="list-disc space-y-1 pl-5 marker:text-blue-500">
  <li>First</li><li>Second</li>
</ul>

<ol class="list-decimal list-inside space-y-2">...</ol>

<ul class="space-y-3">
  <li class="flex gap-3"><svg class="mt-1 size-5 shrink-0 text-green-500">...</svg>Feature with a check icon</li>
</ul>
```

---

## 17. Tables

| Class | CSS |
|---|---|
| `border-collapse` | merge adjacent borders (common for clean tables) |
| `border-separate` | separate borders (needed for rounded corners and spacing) |
| `border-spacing-2`, `border-spacing-x-4`, `border-spacing-y-2` | gap between cells (with `border-separate`) |
| `table-auto` | column widths follow content (default) |
| `table-fixed` | equal/specified widths, faster, enables `truncate` in cells |
| `caption-top` | caption above the table (default) |
| `caption-bottom` | caption below |

```html
<div class="overflow-x-auto rounded-lg border border-gray-200">
  <table class="min-w-full border-collapse text-left text-sm">
    <caption class="caption-bottom p-3 text-xs text-gray-500">Monthly users</caption>
    <thead class="bg-gray-50 text-xs uppercase tracking-wider text-gray-500">
      <tr><th class="px-4 py-3">Name</th><th class="px-4 py-3">Role</th><th class="px-4 py-3 text-right">Status</th></tr>
    </thead>
    <tbody class="divide-y divide-gray-200">
      <tr class="hover:bg-gray-50 odd:bg-white even:bg-gray-50/50">
        <td class="px-4 py-3 font-medium text-gray-900">Ada</td>
        <td class="px-4 py-3 text-gray-600">Admin</td>
        <td class="px-4 py-3 text-right"><span class="rounded-full bg-green-100 px-2 py-0.5 text-xs text-green-700">Active</span></td>
      </tr>
    </tbody>
  </table>
</div>
```

---

## 18. Forms / Inputs

Tailwind removes the browser's default form styling, so you style everything yourself. (Optionally add the official plugin: `@plugin "@tailwindcss/forms";` in your CSS to get nicer defaults.)

### 18.1 Form State Variants

| Variant | Applies when |
|---|---|
| `focus:` | element is focused (mouse or keyboard) |
| `focus-visible:` | focus from the keyboard (best for buttons and links) |
| `focus-within:` | any child has focus (style a wrapper) |
| `hover:` / `active:` | pointer over / pressed |
| `disabled:` | `disabled` attribute present |
| `required:` / `optional:` | has / lacks `required` |
| `invalid:` | fails validation (shows immediately) |
| `user-invalid:` / `user-valid:` | invalid / valid **after user interaction** (v4.1+; nicer than `invalid:`) |
| `valid:` | passes validation |
| `checked:` | checkbox/radio checked |
| `indeterminate:` | indeterminate checkbox |
| `placeholder:` | the placeholder text itself (`placeholder:text-gray-400`) |
| `placeholder-shown:` | input is currently showing its placeholder (empty) |
| `read-only:` | `readonly` attribute |
| `autofill:` | browser autofilled |
| `file:` | the "Choose file" button of `<input type="file">` |
| `aria-invalid:` | `aria-invalid="true"` |

### 18.2 Text Input

```html
<label class="block">
  <span class="mb-1 block text-sm font-medium text-gray-700">Email</span>
  <input
    type="email"
    placeholder="you@example.com"
    class="block w-full rounded-lg border border-gray-300 bg-white px-3 py-2 text-gray-900
           placeholder:text-gray-400
           focus:border-blue-500 focus:outline-hidden focus:ring-3 focus:ring-blue-500/30
           disabled:cursor-not-allowed disabled:bg-gray-100 disabled:text-gray-500
           user-invalid:border-red-500 user-invalid:ring-red-500/30"
  />
</label>
```

### 18.3 Textarea

```html
<textarea rows="4" class="w-full resize-y rounded-lg border border-gray-300 p-3
  focus:border-blue-500 focus:outline-hidden focus:ring-3 focus:ring-blue-500/30"></textarea>

<!-- Auto-growing textarea (v4) -->
<textarea class="field-sizing-content min-h-20 w-full rounded-lg border p-3"></textarea>
```

Use `resize-none` to disable resizing, `resize-y` vertical only, `resize-x`, `resize`.

### 18.4 Select

```html
<select class="w-full appearance-none rounded-lg border border-gray-300 bg-white px-3 py-2
               focus:border-blue-500 focus:outline-hidden focus:ring-3 focus:ring-blue-500/30">
  <option>One</option><option>Two</option>
</select>
```

`appearance-none` removes the native arrow. Add your own icon positioned with `absolute` and `pointer-events-none`.

### 18.5 Checkbox and Radio

```html
<!-- Simple: color the native control with accent- -->
<label class="flex items-center gap-2">
  <input type="checkbox" class="size-4 rounded accent-blue-600" />
  <span class="text-sm">Remember me</span>
</label>

<label class="flex items-center gap-2">
  <input type="radio" name="plan" class="size-4 accent-blue-600" />
  <span class="text-sm">Monthly</span>
</label>

<!-- Fully custom checkbox using appearance-none + checked: -->
<input type="checkbox"
  class="size-5 appearance-none rounded border border-gray-300 bg-white
         checked:border-blue-600 checked:bg-blue-600
         focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2" />
```

### 18.6 Buttons

```html
<button type="button"
  class="inline-flex items-center justify-center gap-2 rounded-lg bg-blue-600 px-4 py-2
         font-medium text-white shadow-sm cursor-pointer transition
         hover:bg-blue-700 active:scale-95
         focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600
         disabled:cursor-not-allowed disabled:opacity-50">
  Save
</button>
```

### 18.7 File Input

```html
<input type="file" class="block w-full text-sm text-gray-500
  file:mr-4 file:rounded-full file:border-0 file:bg-blue-50 file:px-4 file:py-2
  file:text-sm file:font-semibold file:text-blue-700 hover:file:bg-blue-100" />
```

### 18.8 Range, Switch and Misc

```html
<input type="range" class="w-full accent-blue-600" />

<!-- Toggle switch with a peer (see Section 25) -->
<label class="relative inline-flex cursor-pointer items-center">
  <input type="checkbox" class="peer sr-only" />
  <div class="h-6 w-11 rounded-full bg-gray-300 transition peer-checked:bg-blue-600
              after:absolute after:left-0.5 after:top-0.5 after:size-5 after:rounded-full after:bg-white
              after:transition peer-checked:after:translate-x-5
              peer-focus-visible:ring-2 peer-focus-visible:ring-blue-500"></div>
</label>
```

### 18.9 Complete Form Example

```html
<form class="mx-auto max-w-md space-y-5 rounded-2xl bg-white p-8 shadow-lg">
  <h2 class="text-2xl font-bold text-gray-900">Contact us</h2>

  <div>
    <label for="name" class="mb-1 block text-sm font-medium text-gray-700">Name</label>
    <input id="name" required class="w-full rounded-lg border border-gray-300 px-3 py-2
      focus:border-blue-500 focus:outline-hidden focus:ring-3 focus:ring-blue-500/30" />
  </div>

  <div>
    <label for="msg" class="mb-1 block text-sm font-medium text-gray-700">Message</label>
    <textarea id="msg" rows="4" class="w-full rounded-lg border border-gray-300 px-3 py-2
      focus:border-blue-500 focus:outline-hidden focus:ring-3 focus:ring-blue-500/30"></textarea>
  </div>

  <label class="flex items-center gap-2 text-sm text-gray-600">
    <input type="checkbox" class="size-4 rounded accent-blue-600" /> I agree to the terms
  </label>

  <button class="w-full rounded-lg bg-blue-600 py-2.5 font-semibold text-white
    hover:bg-blue-700 focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2
    disabled:opacity-50">Send</button>
</form>
```

---

## 19. Interactivity

### 19.1 Cursor

`cursor-auto`, `cursor-default`, `cursor-pointer`, `cursor-wait`, `cursor-text`, `cursor-move`, `cursor-help`, `cursor-not-allowed`, `cursor-none`, `cursor-context-menu`, `cursor-progress`, `cursor-cell`, `cursor-crosshair`, `cursor-vertical-text`, `cursor-alias`, `cursor-copy`, `cursor-no-drop`, `cursor-grab`, `cursor-grabbing`, `cursor-all-scroll`, `cursor-col-resize`, `cursor-row-resize`, `cursor-n-resize`, `cursor-e-resize`, `cursor-s-resize`, `cursor-w-resize`, `cursor-ne-resize`, `cursor-nw-resize`, `cursor-se-resize`, `cursor-sw-resize`, `cursor-ew-resize`, `cursor-ns-resize`, `cursor-nesw-resize`, `cursor-nwse-resize`, `cursor-zoom-in`, `cursor-zoom-out`.

> **Tailwind v3 note:** v4 buttons use `cursor: default` (like native). Add `cursor-pointer` to clickable buttons yourself.

### 19.2 Pointer Events, User Select, Resize, Appearance

| Class | CSS | Use |
|---|---|---|
| `pointer-events-none` | clicks pass through | decorative overlays, disabled look |
| `pointer-events-auto` | restore clicks | child inside a `pointer-events-none` parent |
| `select-none` | cannot select text | buttons, UI labels |
| `select-text` | selectable | |
| `select-all` | one click selects all | copyable codes |
| `select-auto` | default | |
| `resize` / `resize-x` / `resize-y` / `resize-none` | textarea resize handle | |
| `appearance-none` | remove native styling | custom select/checkbox |
| `appearance-auto` | restore | |
| `touch-none`, `touch-auto`, `touch-pan-x`, `touch-pan-y`, `touch-manipulation` | touch gestures | |
| `will-change-auto`, `will-change-transform`, `will-change-scroll`, `will-change-contents` | performance hint | animation-heavy elements |

### 19.3 Scroll Behavior and Snap

| Class | Effect |
|---|---|
| `scroll-smooth` | smooth anchor scrolling (put on `<html>`) |
| `scroll-auto` | instant scroll |
| `scroll-m-*`, `scroll-mt-20` | scroll margin (offset for sticky headers on anchor jumps) |
| `scroll-p-*`, `scroll-pt-4` | scroll padding on the container |
| `snap-x`, `snap-y`, `snap-both`, `snap-none` | enable snap axis on the container |
| `snap-mandatory`, `snap-proximity` | snap strictness |
| `snap-start`, `snap-center`, `snap-end`, `snap-align-none` | where children align |
| `snap-always`, `snap-normal` | don't skip / allow skip |
| `overscroll-contain` | stop scroll chaining |

### 19.4 Caret and Accent

`caret-blue-500` colors the text cursor in inputs. `accent-blue-600` colors native checkboxes, radios, range sliders and progress bars. Both support `/opacity` and arbitrary values: `caret-[#f43f5e]`, `accent-pink-500`.

```html
<input class="caret-pink-500 focus:outline-hidden" />
<input type="checkbox" class="accent-emerald-500" />
<div class="select-none cursor-grab active:cursor-grabbing">Draggable</div>
```


---

## 20. Transitions & Animation

### 20.1 Transition Property

| Class | Transitions |
|---|---|
| `transition` | a sensible default set (colors, opacity, shadow, transform, filters...) |
| `transition-all` | every property (convenient but can hurt performance) |
| `transition-colors` | color, background-color, border-color, text-decoration, fill, stroke |
| `transition-opacity` | opacity |
| `transition-shadow` | box-shadow |
| `transition-transform` | transform (scale, rotate, translate) |
| `transition-none` | no transition |
| `transition-discrete` | allows `display`/discrete properties to switch during transitions (v4) |
| `transition-[width]` | arbitrary property list |

### 20.2 Duration, Timing, Delay

| Duration | Class | Timing function | Class |
|---|---|---|---|
| 75ms | `duration-75` | linear | `ease-linear` |
| 100ms | `duration-100` | slow to fast | `ease-in` |
| 150ms (default) | `duration-150` | fast to slow | `ease-out` |
| 200ms | `duration-200` | slow, fast, slow | `ease-in-out` |
| 300ms | `duration-300` | custom | `ease-[cubic-bezier(0.4,0,0.2,1)]` |
| 500ms | `duration-500` | | |
| 700ms | `duration-700` | | |
| 1000ms | `duration-1000` | | |
| custom | `duration-[2s]` | | |

**Delay:** `delay-75`, `delay-100`, `delay-150`, `delay-200`, `delay-300`, `delay-500`, `delay-700`, `delay-1000`, `delay-[250ms]`.

Rule of thumb: UI feedback (hover, press) `duration-150` to `duration-200`; panels and menus `duration-300`; big motion `duration-500+`.

```html
<button class="bg-blue-500 transition-colors duration-200 ease-out hover:bg-blue-600">Hover me</button>
<div class="transition-transform duration-300 hover:-translate-y-1 hover:shadow-lg">Lift card</div>
<div class="transition-all duration-500 delay-100 opacity-0 translate-y-4 group-hover:opacity-100 group-hover:translate-y-0">Reveal</div>
```

### 20.3 Built-in Animations

| Class | Effect | Use |
|---|---|---|
| `animate-spin` | continuous rotation | loading spinner |
| `animate-ping` | expanding fading ring | notification dot |
| `animate-pulse` | gentle fading in and out | skeleton loaders |
| `animate-bounce` | bouncing | scroll hint arrow |
| `animate-none` | removes animation | reset or reduced motion |
| `animate-[wiggle_1s_ease-in-out_infinite]` | arbitrary animation | uses your `@keyframes` |

```html
<svg class="size-5 animate-spin text-white" viewBox="0 0 24 24" fill="none">
  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z" />
</svg>

<span class="relative flex size-3">
  <span class="absolute inline-flex size-full animate-ping rounded-full bg-sky-400 opacity-75"></span>
  <span class="relative inline-flex size-3 rounded-full bg-sky-500"></span>
</span>
```

### 20.4 Custom Animations (concept)

Define the animation in `@theme` (keyframes go inside it), and Tailwind creates an `animate-*` utility:

```css
@import "tailwindcss";

@theme {
  --animate-wiggle: wiggle 1s ease-in-out infinite;

  @keyframes wiggle {
    0%, 100% { transform: rotate(-3deg); }
    50%      { transform: rotate(3deg); }
  }
}
```

```html
<div class="animate-wiggle">Wiggles forever</div>
<div class="hover:animate-wiggle">Wiggles on hover</div>
```

> **Tailwind v3 note:** v3 defined `keyframes` and `animation` inside `tailwind.config.js` (`theme.extend`).

### 20.5 Animation Accessibility and Entry Animations

| Variant | Purpose |
|---|---|
| `motion-safe:` | apply only if the user has **not** requested reduced motion |
| `motion-reduce:` | apply when the user prefers reduced motion |
| `starting:` | style an element's **first frame** for enter transitions (v4), for example `starting:opacity-0` |

```html
<div class="motion-safe:animate-bounce motion-reduce:animate-none">Respectful animation</div>
<div class="transition-opacity duration-500 starting:opacity-0">Fades in when added to the DOM</div>
```

---

## 21. Transform

In v4 Tailwind uses the individual CSS properties `scale`, `rotate` and `translate`, so these utilities **combine freely** without a `transform` class.

### 21.1 Scale, Rotate, Translate, Skew

| Purpose | Classes | Examples |
|---|---|---|
| Scale (both axes) | `scale-0`, `scale-50`, `scale-75`, `scale-90`, `scale-95`, `scale-100`, `scale-105`, `scale-110`, `scale-125`, `scale-150` | `hover:scale-105` |
| Scale one axis | `scale-x-*`, `scale-y-*` | `scale-x-0`, `scale-y-110` |
| Negative / flip | `-scale-x-100` (mirror horizontally) | |
| Rotate | `rotate-0`, `rotate-1`, `rotate-2`, `rotate-3`, `rotate-6`, `rotate-12`, `rotate-45`, `rotate-90`, `rotate-180` | `rotate-45` |
| Rotate negative | `-rotate-45`, `-rotate-90`... | |
| Translate X | `translate-x-{n}`, `-translate-x-{n}`, `translate-x-1/2`, `-translate-x-full` | `-translate-x-1/2` |
| Translate Y | `translate-y-{n}`, `-translate-y-{n}`, `translate-y-1/2`, `translate-y-full` | `hover:-translate-y-1` |
| Skew | `skew-x-{0,1,2,3,6,12}`, `skew-y-*`, negatives | `-skew-x-12` |
| Arbitrary | `rotate-[17deg]`, `translate-x-[30px]`, `scale-[1.15]` | |
| Reset | `transform-none` | |

### 21.2 Transform Origin

`origin-center` (default), `origin-top`, `origin-top-right`, `origin-right`, `origin-bottom-right`, `origin-bottom`, `origin-bottom-left`, `origin-left`, `origin-top-left`, `origin-[30%_10%]`.

Example: a dropdown that grows from its top-left corner: `origin-top-left scale-95 opacity-0 group-hover:scale-100 group-hover:opacity-100 transition`.

### 21.3 3D Transforms (v4)

`transform-3d`, `perspective-normal`, `perspective-distant`, `rotate-x-12`, `rotate-y-12`, `translate-z-4`, `backface-hidden`, `transform-flat`. Useful for card-flip effects.

### 21.4 Transform Recipes

```html
<!-- Hover grow -->
<div class="transition-transform duration-200 hover:scale-105">Card</div>

<!-- Lift on hover -->
<div class="transition duration-200 hover:-translate-y-1 hover:shadow-xl">Card</div>

<!-- Press effect -->
<button class="transition active:scale-95">Press me</button>

<!-- Rotate icon when open (with group or aria) -->
<svg class="size-5 transition-transform group-open:rotate-180">...</svg>

<!-- Tilted decorative card -->
<div class="rotate-3 rounded-xl bg-yellow-200 p-6 shadow-md">Sticky note</div>

<!-- Center with translate -->
<div class="absolute left-1/2 top-1/2 -translate-x-1/2 -translate-y-1/2">Center</div>

<!-- Slide-in drawer -->
<aside class="fixed inset-y-0 left-0 w-64 -translate-x-full transition-transform data-[open=true]:translate-x-0">...</aside>
```

---

## 22. Filters & Visual Effects

### 22.1 Filter Utilities (apply to the element)

| Effect | Classes |
|---|---|
| Blur | `blur-none`, `blur-xs` (4px), `blur-sm` (8px), `blur-md` (12px), `blur-lg` (16px), `blur-xl` (24px), `blur-2xl` (40px), `blur-3xl` (64px), `blur-[2px]` |
| Brightness | `brightness-0`, `50`, `75`, `90`, `95`, `100`, `105`, `110`, `125`, `150`, `200` |
| Contrast | `contrast-0`, `50`, `75`, `100`, `125`, `150`, `200` |
| Grayscale | `grayscale` (100%), `grayscale-0`, `grayscale-50` |
| Hue rotate | `hue-rotate-15`, `30`, `60`, `90`, `180`, `-hue-rotate-15` |
| Invert | `invert` (100%), `invert-0`, `invert-50` |
| Saturate | `saturate-0`, `50`, `100`, `150`, `200` |
| Sepia | `sepia`, `sepia-0`, `sepia-50` |
| Drop shadow | `drop-shadow-2xs`, `drop-shadow-xs`, `drop-shadow-sm`, `drop-shadow-md`, `drop-shadow-lg`, `drop-shadow-xl`, `drop-shadow-2xl`, `drop-shadow-none`, `drop-shadow-blue-500/50` |
| Remove all | `filter-none` |

`drop-shadow-*` follows the **visible shape** (works on transparent PNGs and SVGs), unlike `shadow-*` which uses the rectangular box.

### 22.2 Backdrop Filters (affect what is behind the element)

| Effect | Classes |
|---|---|
| Backdrop blur | `backdrop-blur-none`, `backdrop-blur-xs`, `backdrop-blur-sm`, `backdrop-blur-md`, `backdrop-blur-lg`, `backdrop-blur-xl`, `backdrop-blur-2xl`, `backdrop-blur-3xl` |
| Brightness | `backdrop-brightness-50`, `75`, `90`, `100`, `110`, `125`, `150`, `200` |
| Contrast | `backdrop-contrast-50`, `75`, `100`, `125`, `150`, `200` |
| Grayscale | `backdrop-grayscale`, `backdrop-grayscale-0` |
| Hue rotate | `backdrop-hue-rotate-15`, `30`, `60`, `90`, `180` |
| Invert | `backdrop-invert`, `backdrop-invert-0` |
| Opacity | `backdrop-opacity-0` ... `backdrop-opacity-100` |
| Saturate | `backdrop-saturate-0`, `50`, `100`, `150`, `200` |
| Sepia | `backdrop-sepia`, `backdrop-sepia-0` |
| Remove all | `backdrop-filter-none` |

> **Tailwind v3 note:** v3 needed `filter` and `backdrop-filter` helper classes. In v4 they are applied automatically; you only write `blur-sm` or `backdrop-blur-md`. Also v3 `blur`/`drop-shadow` (bare) became `blur-sm`/`drop-shadow-sm`.

### 22.3 Glassmorphism Examples

```html
<!-- Frosted glass card over a colorful background -->
<div class="relative min-h-screen bg-linear-to-br from-indigo-500 via-purple-500 to-pink-500 grid place-items-center p-6">
  <div class="w-full max-w-sm rounded-2xl border border-white/30 bg-white/20 p-8 text-white
              shadow-xl backdrop-blur-lg backdrop-saturate-150">
    <h2 class="text-2xl font-bold">Glass card</h2>
    <p class="mt-2 text-white/80">Blurred background shines through.</p>
  </div>
</div>

<!-- Frosted sticky navbar -->
<header class="sticky top-0 z-20 border-b border-white/20 bg-white/70 backdrop-blur-md dark:bg-gray-900/70">...</header>

<!-- Dark glass -->
<div class="rounded-xl border border-white/10 bg-black/30 backdrop-blur-xl">...</div>

<!-- Dim and blur the page behind a modal -->
<div class="fixed inset-0 bg-black/40 backdrop-blur-sm"></div>

<!-- Disabled image look -->
<img class="grayscale opacity-60" />

<!-- Image zoom with brightness on hover -->
<img class="transition duration-300 hover:scale-105 hover:brightness-110" />
```

---

## 23. Responsive Design

### 23.1 Mobile-First: The Key Idea

Un-prefixed utilities apply to **all screen sizes** (mobile first). Prefixed utilities (`md:`) apply **from that breakpoint upward**. So you style the **smallest screen first**, then add overrides for larger screens.

```html
<!-- Mobile: small text, 1 column. md+: bigger text, 2 columns. lg+: 3 columns -->
<h1 class="text-sm md:text-lg lg:text-2xl">Responsive text</h1>
<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">...</div>
```

```text
screen width:  0 ------- 640 ------- 768 ------- 1024 ------- 1280 ------- 1536 ---->
class:         (none)      sm:         md:         lg:          xl:          2xl:
               always on   640+        768+        1024+        1280+        1536+
```

> **Wrong thinking:** `sm:` does **not** mean "small screens only". It means "640px and up". To target phones, use the un-prefixed class.

### 23.2 Breakpoints

| Prefix | Min-width | CSS media query |
|---|---|---|
| `sm:` | 640px (40rem) | `@media (width >= 40rem)` |
| `md:` | 768px (48rem) | `@media (width >= 48rem)` |
| `lg:` | 1024px (64rem) | `@media (width >= 64rem)` |
| `xl:` | 1280px (80rem) | `@media (width >= 80rem)` |
| `2xl:` | 1536px (96rem) | `@media (width >= 96rem)` |

### 23.3 Max-Width Variants and Ranges

| Variant | Applies when | Equivalent |
|---|---|---|
| `max-sm:` | width **below** 640px | `@media (width < 40rem)` |
| `max-md:` | below 768px | |
| `max-lg:` | below 1024px | |
| `max-xl:` | below 1280px | |
| `max-2xl:` | below 1536px | |
| `md:max-lg:` | **between** 768px and 1023px | range (stack variants) |
| `min-[900px]:` | at least 900px (arbitrary) | |
| `max-[600px]:` | below 600px (arbitrary) | |

```html
<div class="max-md:hidden">Hidden below 768px</div>
<div class="md:max-lg:grid-cols-2 grid grid-cols-1 lg:grid-cols-4">Two columns only on tablets</div>
```

### 23.4 Container Queries (v4 built-in)

Respond to the **parent's** width instead of the viewport. Mark the parent with `@container`, then use `@sm:`, `@md:`, `@lg:` ... on children.

```html
<div class="@container">
  <div class="flex flex-col @md:flex-row @md:items-center gap-4">
    Layout changes based on the card's width, not the screen
  </div>
</div>
```

Sizes: `@3xs` (16rem), `@2xs`, `@xs`, `@sm` (24rem), `@md` (28rem), `@lg` (32rem), `@xl`, `@2xl`, ... `@7xl`; max versions `@max-md:`; named containers `@container/card` + `@md/card:`.

### 23.5 Custom Breakpoints

```css
@theme { --breakpoint-3xl: 120rem; }   /* creates 3xl: and max-3xl: */
```

### 23.6 Responsive Patterns

```html
<!-- Stack on mobile, row on desktop -->
<div class="flex flex-col gap-6 md:flex-row">
  <div class="md:w-1/3">Sidebar</div>
  <div class="md:w-2/3">Content</div>
</div>

<!-- Show hamburger on mobile, menu on desktop -->
<button class="md:hidden">Menu</button>
<ul class="hidden md:flex gap-6">...</ul>

<!-- Responsive padding and type -->
<section class="px-4 py-12 sm:px-6 md:py-20 lg:px-8">
  <h2 class="text-2xl font-bold sm:text-3xl lg:text-5xl">Title</h2>
</section>

<!-- Centered container with a max width -->
<div class="mx-auto w-full max-w-7xl px-4">...</div>

<!-- Responsive image -->
<img class="h-48 w-full object-cover md:h-72 lg:h-96" />

<!-- Reorder on mobile -->
<div class="flex flex-col md:flex-row"><div class="order-2 md:order-1">A</div><div class="order-1 md:order-2">B</div></div>
```

**Testing tip:** use browser DevTools device mode and try widths 375, 768, 1024 and 1440.

---

## 24. State Variants

Any utility can be prefixed with a variant. Variants can be **stacked** (applied left to right): `md:dark:hover:bg-blue-700`.

### 24.1 Interaction States

| Variant | When | Example |
|---|---|---|
| `hover:` | pointer over (only on devices that support hover in v4) | `hover:bg-blue-600` |
| `focus:` | element has focus | `focus:ring-2` |
| `focus-visible:` | keyboard focus | `focus-visible:outline-2` |
| `focus-within:` | a descendant has focus | `focus-within:ring-2` |
| `active:` | being pressed | `active:scale-95` |
| `visited:` | visited link | `visited:text-purple-600` |
| `target:` | element is the URL `#hash` target | `target:bg-yellow-100` |
| `open:` | `<details>`/`<dialog>`/popover is open | `open:bg-gray-50` |

### 24.2 Form States

| Variant | When | Example |
|---|---|---|
| `disabled:` | disabled | `disabled:opacity-50` |
| `enabled:` | not disabled | `enabled:hover:bg-blue-700` |
| `checked:` | checked box/radio | `checked:bg-blue-600` |
| `indeterminate:` | indeterminate checkbox | `indeterminate:bg-gray-400` |
| `default:` | default-selected option/checkbox | `default:ring-2` |
| `required:` | `required` | `required:border-red-300` |
| `optional:` | not required | |
| `valid:` | valid value | `valid:border-green-500` |
| `invalid:` | invalid value | `invalid:border-red-500` |
| `user-valid:` / `user-invalid:` | valid/invalid after interaction (v4.1+) | `user-invalid:border-red-500` |
| `in-range:` | value within min/max | `in-range:border-green-500` |
| `out-of-range:` | value outside min/max | `out-of-range:border-red-500` |
| `placeholder-shown:` | placeholder visible (input empty) | `placeholder-shown:border-gray-300` |
| `autofill:` | browser autofill | `autofill:bg-yellow-50` |
| `read-only:` | `readonly` | `read-only:bg-gray-100` |
| `read-write:` | editable | |

### 24.3 Structural (position in the DOM)

| Variant | Selects | Example |
|---|---|---|
| `first:` | first child | `first:pt-0` |
| `last:` | last child | `last:border-b-0` |
| `only:` | only child | `only:rounded-lg` |
| `odd:` / `even:` | odd / even children | `odd:bg-gray-50` |
| `first-of-type:` / `last-of-type:` / `only-of-type:` | by element type | `first-of-type:mt-0` |
| `empty:` | no children / no text | `empty:hidden` |
| `nth-3:` / `nth-[3n+1]:` | nth-child | `nth-[3n+1]:bg-gray-50` |
| `has-[...]:` | parent that contains a match | `has-[:checked]:bg-blue-50` |
| `not-*:` | negation | `not-first:mt-4`, `not-hover:opacity-70` |
| `*:` | all **direct children** | `*:p-2` |
| `**:` | all descendants (v4.1+) | `**:text-sm` |

### 24.4 Pseudo-elements

| Variant | Target | Example |
|---|---|---|
| `before:` / `after:` | `::before` / `::after` (auto-adds `content: ''`) | `after:absolute after:inset-0` |
| `placeholder:` | placeholder text | `placeholder:italic` |
| `file:` | file input button | `file:bg-blue-50` |
| `marker:` | list marker | `marker:text-blue-500` |
| `selection:` | selected text | `selection:bg-yellow-200` |
| `first-letter:` / `first-line:` | text fragments | `first-letter:text-5xl` |
| `backdrop:` | `<dialog>` backdrop | `backdrop:bg-black/50` |

### 24.5 Attribute, Media and Other Variants

| Variant | Purpose | Example |
|---|---|---|
| `aria-checked:`, `aria-expanded:`, `aria-disabled:`, `aria-[sort=ascending]:` | ARIA attributes | `aria-expanded:rotate-180` |
| `data-[state=open]:` | data attributes | `data-[active=true]:bg-blue-500` |
| `data-active:` | presence of `data-active` | |
| `dark:` | dark mode | `dark:bg-gray-900` |
| `motion-safe:` / `motion-reduce:` | reduced motion | |
| `print:` | printing | `print:hidden` |
| `portrait:` / `landscape:` | orientation | |
| `rtl:` / `ltr:` | text direction | `rtl:space-x-reverse` |
| `supports-[display:grid]:` | feature queries | |
| `contrast-more:` | high-contrast preference | |
| `forced-colors:` | forced colors mode | |
| `pointer-fine:` / `pointer-coarse:` | mouse vs touch | `pointer-coarse:p-4` |
| `starting:` | entry animations | `starting:opacity-0` |
| `group-*` / `peer-*` | parent/sibling state | [Section 25](#25-group--peer) |
| `[&:nth-child(3)]:` | arbitrary selector | `[&>li]:py-2` |

### 24.6 Practical State Examples

```html
<!-- Link states -->
<a class="text-blue-600 underline-offset-4 hover:underline focus-visible:outline-2 visited:text-purple-600">Link</a>

<!-- Zebra rows + borders between all but last -->
<ul>
  <li class="odd:bg-gray-50 border-b last:border-b-0 p-3">Row</li>
</ul>

<!-- Hide empty state container -->
<div class="empty:hidden">{maybeContent}</div>

<!-- Highlight a label when its checkbox is checked -->
<label class="flex items-center gap-2 rounded-lg border p-3 has-[:checked]:border-blue-500 has-[:checked]:bg-blue-50">
  <input type="checkbox" /> Option
</label>

<!-- Drop cap -->
<p class="first-letter:float-left first-letter:mr-2 first-letter:text-5xl first-letter:font-bold">Once upon a time...</p>

<!-- Style based on a data attribute (great with React state) -->
<button data-active={isActive} class="data-[active=true]:bg-blue-600 data-[active=true]:text-white">Tab</button>

<!-- Space children except the first -->
<div class="[&>*:not(:first-child)]:mt-4">...</div>
```

---

## 25. Group & Peer

### 25.1 Group: style children based on the PARENT'S state

Add `group` to the parent. On the child use `group-hover:`, `group-focus:`, `group-active:`, `group-disabled:`, `group-focus-within:`, `group-has-[...]:`, `group-open:`, `group-first:`, `group-odd:`, `group-aria-*:`, `group-data-*:`...

```html
<!-- Card hover affects children -->
<a href="#" class="group block rounded-xl border p-6 transition hover:border-blue-500 hover:shadow-lg">
  <h3 class="font-semibold text-gray-900 group-hover:text-blue-600">Title</h3>
  <p class="text-gray-500 group-hover:text-gray-700">Description</p>
  <span class="mt-4 inline-block transition-transform group-hover:translate-x-1">Read more &rarr;</span>
</a>

<!-- Image zoom inside a clipped card -->
<div class="group overflow-hidden rounded-xl">
  <img class="transition duration-500 group-hover:scale-110" src="..." alt="" />
</div>

<!-- Show actions on row hover -->
<li class="group flex items-center justify-between p-3 hover:bg-gray-50">
  <span>Item</span>
  <button class="opacity-0 transition group-hover:opacity-100">Delete</button>
</li>

<!-- Details/accordion arrow -->
<details class="group">
  <summary class="flex cursor-pointer items-center justify-between">Question
    <svg class="size-4 transition-transform group-open:rotate-180">...</svg>
  </summary>
  <p>Answer</p>
</details>
```

**Named groups (nested groups):** give each group a name with `group/name`, then use `group-hover/name:`.

```html
<ul>
  <li class="group/item hover:bg-gray-50">
    <a class="group/edit invisible group-hover/item:visible hover:bg-slate-200">
      <span class="group-hover/edit:text-gray-700">Call</span>
    </a>
  </li>
</ul>
```

### 25.2 Peer: style an element based on a SIBLING'S state

Add `peer` to the **earlier** sibling. The styled element must come **after** it in the DOM and use `peer-checked:`, `peer-focus:`, `peer-invalid:`, `peer-hover:`, `peer-disabled:`, `peer-placeholder-shown:`, `peer-required:`, `peer-has-[...]:`...

```html
<!-- Show an error message when the input is invalid -->
<input type="email" required class="peer w-full rounded border px-3 py-2 invalid:border-red-500" />
<p class="mt-1 hidden text-sm text-red-600 peer-invalid:block">Please enter a valid email.</p>

<!-- Radio card: highlight the card of the selected radio -->
<label>
  <input type="radio" name="plan" class="peer sr-only" />
  <div class="cursor-pointer rounded-xl border p-4 peer-checked:border-blue-600 peer-checked:bg-blue-50 peer-focus-visible:ring-2">Pro plan</div>
</label>

<!-- Floating label input -->
<div class="relative">
  <input id="email" placeholder=" "
    class="peer w-full rounded-lg border border-gray-300 px-3 pb-2 pt-5 focus:border-blue-500 focus:outline-hidden" />
  <label for="email"
    class="pointer-events-none absolute left-3 top-4 origin-left text-gray-500 transition-all duration-200
           peer-focus:top-1.5 peer-focus:text-xs peer-focus:text-blue-600
           peer-[:not(:placeholder-shown)]:top-1.5 peer-[:not(:placeholder-shown)]:text-xs">
    Email
  </label>
</div>
```

Floating label trick: the input has `placeholder=" "` (a single space) so `:placeholder-shown` tells whether it is empty.

**Peer rules:** the `peer` element must be a **previous sibling** (CSS can only look forward). With several peers, name them: `peer/email` and `peer-invalid/email:`.

---

## 26. Dark Mode

### 26.1 The dark: Variant

```html
<div class="bg-white text-gray-900 dark:bg-gray-900 dark:text-white">
  <p class="text-gray-600 dark:text-gray-400">Adapts to dark mode</p>
  <button class="bg-blue-600 hover:bg-blue-700 dark:bg-blue-500 dark:hover:bg-blue-400">Button</button>
  <div class="border-gray-200 dark:border-gray-700 border">Card</div>
</div>
```

### 26.2 How Dark Mode Works in v4

**Default (automatic):** `dark:` follows the user's operating system preference through `@media (prefers-color-scheme: dark)`. No setup needed.

**Manual toggle (class-based):** override the variant in your CSS, then add or remove the class `dark` on `<html>`:

```css
@import "tailwindcss";
@custom-variant dark (&:where(.dark, .dark *));
```

**Using a data attribute instead:**

```css
@custom-variant dark (&:where([data-theme=dark], [data-theme=dark] *));
```

> **Tailwind v3 note:** v3 used `darkMode: 'class'` (or `'media'`) in `tailwind.config.js`. In v4 you use `@custom-variant dark` in CSS.

### 26.3 React Dark Mode Toggle

```jsx
import { useEffect, useState } from 'react'

export default function ThemeToggle() {
  const [dark, setDark] = useState(
    () => localStorage.theme === 'dark' ||
          (!('theme' in localStorage) && window.matchMedia('(prefers-color-scheme: dark)').matches)
  )

  useEffect(() => {
    document.documentElement.classList.toggle('dark', dark)
    localStorage.theme = dark ? 'dark' : 'light'
  }, [dark])

  return (
    <button onClick={() => setDark(!dark)}
      className="rounded-lg border px-3 py-1.5 text-sm dark:border-gray-600 dark:text-white">
      {dark ? 'Light' : 'Dark'} mode
    </button>
  )
}
```

(Requires the `@custom-variant dark` line above.)

### 26.4 Dark Mode Tips

- Pair every background with a text color: `bg-white text-gray-900 dark:bg-gray-900 dark:text-gray-100`.
- Dark surfaces: `gray-900`/`gray-950`; borders: `gray-700`/`gray-800`; muted text: `gray-400`.
- Lower the intensity of saturated colors in dark mode (use `400` instead of `600` for text accents).
- Define semantic color tokens once with CSS variables to avoid repeating `dark:` everywhere:

```css
:root { --surface: white; --ink: #111827; }
.dark { --surface: #0b1220; --ink: #f3f4f6; }
@theme inline { --color-surface: var(--surface); --color-ink: var(--ink); }
/* now: bg-surface text-ink works in both themes */
```

---

## 27. Arbitrary Values

### 27.1 Arbitrary Values `utility-[value]`

Use square brackets to pass **any CSS value** when the theme has no matching class.

| Class | Generates |
|---|---|
| `w-[350px]` | `width: 350px` |
| `h-[500px]` | `height: 500px` |
| `mt-[37px]` | `margin-top: 37px` |
| `text-[22px]` | `font-size: 22px` |
| `text-[#123456]` / `bg-[#123456]` | colors (Tailwind detects the type) |
| `top-[10px]` | `top: 10px` |
| `grid-cols-[200px_1fr]` | `grid-template-columns: 200px 1fr` |
| `grid-cols-[repeat(auto-fit,minmax(250px,1fr))]` | responsive grid |
| `w-[calc(100%-2rem)]` | `width: calc(100% - 2rem)` |
| `h-[calc(100dvh-4rem)]` | `height: calc(100dvh - 4rem)` |
| `bg-[url(/img/hero.png)]` | background image |
| `shadow-[0_4px_20px_rgba(0,0,0,0.15)]` | custom shadow |
| `rotate-[17deg]` | `rotate: 17deg` |
| `leading-[1.7]` | line-height |
| `tracking-[0.2em]` | letter-spacing |
| `rounded-[10px]` | radius |
| `duration-[2s]` | transition duration |
| `z-[999]` | z-index |
| `font-[Inter]` | font family |
| `content-['hello']` | `content: 'hello'` (with `before:`/`after:`) |
| `w-(--my-width)` | uses CSS variable (v4 shorthand for `w-[var(--my-width)]`) |

**Rules**

- No spaces inside brackets: use `_` instead (`grid-cols-[200px_1fr]`). For a real underscore, escape it `\_`.
- `calc()` works; spaces around `+ - * /` are added for you.
- Add a **type hint** if Tailwind cannot tell the type: `text-[length:var(--size)]`, `text-[color:var(--c)]`, or `text-(length:--size)`.
- Works with variants: `md:w-[500px]`, `hover:bg-[#123456]`, `dark:text-[#e5e7eb]`.
- Negative: `-mt-[10px]` or `mt-[-10px]`.

### 27.2 Arbitrary Properties `[property:value]`

For a CSS property that has no Tailwind utility (or you need it quickly):

```html
<div class="[mask-type:luminance]"></div>
<div class="[--card-gap:12px] gap-(--card-gap)"></div>     <!-- define & use a variable -->
<div class="[clip-path:polygon(50%_0,100%_100%,0_100%)]"></div>
<div class="hover:[mask-type:alpha]"></div>
<div class="[text-wrap:balance]"></div>
```

### 27.3 Arbitrary Variants `[selector]:`

```html
<li class="[&:nth-child(3)]:underline">third item</li>
<ul class="[&>li]:py-2 [&_a]:text-blue-600">...</ul>      <!-- style children without classes on them -->
<div class="[@media(min-width:900px)]:flex">...</div>
<div class="[&.is-active]:font-bold">...</div>
```

`&` stands for the element itself. `[&>li]` = direct `li` children, `[&_a]` = any descendant `a` (underscore = space).

### 27.4 When to Use (and Not Use) Arbitrary Values

| Good use | Bad use |
|---|---|
| A one-off value from a design file (`w-[342px]`) | Repeating the same value 20 times (add a theme token instead) |
| Complex grid templates | Replacing a scale value you could use (`mt-[16px]` instead of `mt-4`) |
| `calc()` layouts | Building a whole design from px values |
| Brand color used once | Brand color used everywhere: define `--color-brand` in `@theme` |
| Quick prototyping | Anything that should stay consistent across the app |

---

## 28. Important Modifier

Adds `!important` to the generated declaration.

| Version | Syntax | Example |
|---|---|---|
| Tailwind v4 (preferred) | **trailing** `!` | `text-red-500!`, `md:p-4!`, `hover:bg-blue-600!` |
| Tailwind v3 (still works in v4, legacy) | **leading** `!` | `!text-red-500` |

```html
<p class="text-gray-500 text-red-500!">Always red, even if something else tries to override it</p>
```

**When it is appropriate**

- Overriding styles from a **third-party library** you cannot edit (date pickers, widgets).
- Forcing a utility to beat styles injected inline or with high specificity.

**When it is NOT appropriate**

- To fix your own conflicting classes (remove or merge them instead: see `tailwind-merge`).
- Everywhere "just in case": it makes later overrides impossible.

---

## 29. Container

### 29.1 The container Class

`container` sets `width: 100%` and a **`max-width` equal to the current breakpoint**:

| Screen | max-width |
|---|---|
| (below sm) | 100% |
| `sm` (640px) | 640px |
| `md` (768px) | 768px |
| `lg` (1024px) | 1024px |
| `xl` (1280px) | 1280px |
| `2xl` (1536px) | 1536px |

It does **not** center itself or add padding by default:

```html
<div class="container mx-auto px-4">...</div>
```

**Most people prefer `max-w-*` for predictable widths:** `mx-auto max-w-7xl px-4 sm:px-6 lg:px-8`.

### 29.2 Customize the container (v4)

```css
@utility container {
  margin-inline: auto;
  padding-inline: 2rem;
}
```

> **Tailwind v3 note:** v3 customized the container in `tailwind.config.js` (`container: { center: true, padding: '2rem' }`). Those options **no longer exist** in v4.

---

## 30. Accessibility

### 30.1 Screen Reader Utilities

| Class | Effect |
|---|---|
| `sr-only` | visually hidden but available to screen readers |
| `not-sr-only` | undo `sr-only` (for example on focus) |
| `forced-color-adjust-none` / `forced-color-adjust-auto` | opt out of / into forced-colors mode |

```html
<!-- Icon-only button needs a text alternative -->
<button class="rounded-full p-2 hover:bg-gray-100">
  <svg class="size-5" aria-hidden="true">...</svg>
  <span class="sr-only">Close menu</span>
</button>

<!-- Skip link: visible only when focused -->
<a href="#main" class="sr-only focus:not-sr-only focus:absolute focus:left-4 focus:top-4 focus:rounded focus:bg-white focus:px-4 focus:py-2">
  Skip to content
</a>
```

### 30.2 Focus States (never remove them without a replacement)

```html
<!-- Good: custom visible focus ring for keyboard users -->
<button class="rounded-lg bg-blue-600 px-4 py-2 text-white outline-hidden
               focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2">Save</button>

<a class="rounded focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-blue-600">Link</a>
```

- Use **`focus-visible:`** (keyboard only) for buttons and links, **`focus:`** for text inputs.
- Use `outline-hidden` (not `outline-none`) when replacing the outline: it stays visible in high-contrast mode.

### 30.3 Accessible Buttons and Forms Checklist

- Real `<button>` for actions and `<a>` for navigation (not clickable `<div>`s).
- Every input has a `<label for="id">` (use `sr-only` if the design hides it).
- Color contrast: text on `bg-white` should be `gray-600` or darker for body text (WCAG AA 4.5:1).
- Do not rely on color alone for errors: add text or an icon.
- Disabled look: `disabled:opacity-50 disabled:cursor-not-allowed` plus the real `disabled` attribute.
- Touch targets: at least ~44x44px (`min-h-11 min-w-11`).
- Respect reduced motion: `motion-safe:animate-spin motion-reduce:animate-none`.
- Use ARIA state variants: `aria-expanded:rotate-180`, `aria-selected:bg-blue-50`, `aria-disabled:opacity-50`.


---

## 31. Common UI Patterns

Ready-to-copy components. They use plain HTML with `class`. **In React, change `class` to `className`, `for` to `htmlFor`, and self-close tags (`<input />`).** Icons are shown as `<svg>...</svg>` placeholders.

### 31.1 Navbar

```html
<header class="sticky top-0 z-30 border-b border-gray-200 bg-white/80 backdrop-blur">
  <nav class="mx-auto flex max-w-7xl items-center justify-between px-4 py-3 sm:px-6 lg:px-8">
    <a href="/" class="text-xl font-bold text-blue-600">Brand</a>

    <ul class="hidden items-center gap-8 text-sm font-medium text-gray-600 md:flex">
      <li><a href="#" class="transition-colors hover:text-gray-900">Home</a></li>
      <li><a href="#" class="transition-colors hover:text-gray-900">Features</a></li>
      <li><a href="#" class="transition-colors hover:text-gray-900">Pricing</a></li>
    </ul>

    <div class="flex items-center gap-3">
      <a href="#" class="hidden text-sm font-medium text-gray-600 hover:text-gray-900 sm:block">Log in</a>
      <a href="#" class="rounded-lg bg-blue-600 px-4 py-2 text-sm font-semibold text-white hover:bg-blue-700">Sign up</a>
      <button class="rounded-lg p-2 hover:bg-gray-100 md:hidden" aria-label="Open menu"><svg class="size-6">...</svg></button>
    </div>
  </nav>
</header>
```

| Important classes | Why |
|---|---|
| `sticky top-0 z-30` | stays at the top while scrolling, above content |
| `bg-white/80 backdrop-blur` | translucent frosted bar |
| `mx-auto max-w-7xl px-4 ...` | centered content column with responsive side padding |
| `flex items-center justify-between` | logo left, actions right, vertically centered |
| `hidden md:flex` | desktop menu hidden on mobile, shown from 768px |
| `md:hidden` | hamburger only on mobile |

### 31.2 Hero Section

```html
<section class="relative isolate overflow-hidden bg-linear-to-b from-indigo-50 to-white">
  <div class="mx-auto max-w-4xl px-4 py-24 text-center sm:py-32">
    <span class="rounded-full bg-indigo-100 px-3 py-1 text-xs font-semibold uppercase tracking-wider text-indigo-700">New release</span>
    <h1 class="mt-6 text-4xl font-bold tracking-tight text-balance text-gray-900 sm:text-6xl">
      Build beautiful interfaces, faster
    </h1>
    <p class="mx-auto mt-6 max-w-2xl text-lg leading-8 text-pretty text-gray-600">
      A short supporting sentence that explains the product value in plain language.
    </p>
    <div class="mt-10 flex flex-col items-center justify-center gap-4 sm:flex-row">
      <a href="#" class="w-full rounded-lg bg-indigo-600 px-6 py-3 font-semibold text-white shadow-sm hover:bg-indigo-500 sm:w-auto">Get started</a>
      <a href="#" class="font-semibold text-gray-900">Learn more <span aria-hidden="true">&rarr;</span></a>
    </div>
  </div>
</section>
```

| Important classes | Why |
|---|---|
| `bg-linear-to-b from-indigo-50 to-white` | soft vertical gradient |
| `text-4xl sm:text-6xl` | mobile-first heading size |
| `tracking-tight text-balance` | polished headline wrapping |
| `mx-auto max-w-2xl` | centered paragraph with a readable width |
| `flex-col sm:flex-row` | buttons stack on phones, sit side by side after 640px |

### 31.3 Profile Card

```html
<div class="mx-auto w-full max-w-sm overflow-hidden rounded-2xl bg-white shadow-lg">
  <div class="h-28 bg-linear-to-r from-blue-500 to-purple-600"></div>
  <div class="px-6 pb-6">
    <img class="-mt-12 size-24 rounded-full border-4 border-white object-cover" src="avatar.jpg" alt="Ada Lovelace" />
    <h3 class="mt-3 text-xl font-bold text-gray-900">Ada Lovelace</h3>
    <p class="text-sm text-gray-500">Frontend Engineer</p>
    <p class="mt-3 text-gray-600">Building accessible interfaces with React and Tailwind.</p>
    <div class="mt-5 flex divide-x divide-gray-200 text-center">
      <div class="flex-1"><p class="font-bold">1.2k</p><p class="text-xs text-gray-500">Followers</p></div>
      <div class="flex-1"><p class="font-bold">340</p><p class="text-xs text-gray-500">Following</p></div>
      <div class="flex-1"><p class="font-bold">87</p><p class="text-xs text-gray-500">Posts</p></div>
    </div>
    <button class="mt-5 w-full rounded-lg bg-blue-600 py-2 font-medium text-white hover:bg-blue-700">Follow</button>
  </div>
</div>
```

| Important classes | Why |
|---|---|
| `overflow-hidden rounded-2xl` | clips the banner to the rounded corners |
| `-mt-12 ... border-4 border-white` | avatar overlaps the banner with a white outline |
| `size-24 rounded-full object-cover` | perfect circle, image cropped not squashed |
| `flex divide-x` | equal stat columns with vertical separators |

### 31.4 Product Card

```html
<div class="group w-full max-w-xs overflow-hidden rounded-xl border border-gray-200 bg-white transition hover:shadow-xl">
  <div class="relative aspect-square overflow-hidden bg-gray-100">
    <img class="size-full object-cover transition duration-500 group-hover:scale-105" src="shoe.jpg" alt="Running shoe" />
    <span class="absolute left-3 top-3 rounded-full bg-red-500 px-2 py-0.5 text-xs font-semibold text-white">-20%</span>
  </div>
  <div class="space-y-2 p-4">
    <h3 class="font-semibold text-gray-900">Aero Runner</h3>
    <p class="line-clamp-2 text-sm text-gray-500">Lightweight running shoe with breathable mesh and responsive foam.</p>
    <div class="flex items-center justify-between pt-2">
      <p><span class="text-lg font-bold text-gray-900">$96</span> <span class="text-sm text-gray-400 line-through">$120</span></p>
      <button class="rounded-lg bg-gray-900 px-3 py-1.5 text-sm font-medium text-white hover:bg-gray-700">Add to cart</button>
    </div>
  </div>
</div>
```

| Important classes | Why |
|---|---|
| `group` + `group-hover:scale-105` | image zooms when the whole card is hovered |
| `aspect-square overflow-hidden` | consistent square image box that clips the zoom |
| `absolute left-3 top-3` | badge pinned to the image corner (parent is `relative`) |
| `line-clamp-2` | description limited to two lines |
| `line-through` | struck-through old price |

### 31.5 Login Form

```html
<div class="grid min-h-dvh place-items-center bg-gray-50 px-4">
  <form class="w-full max-w-sm space-y-5 rounded-2xl bg-white p-8 shadow-lg">
    <div class="text-center">
      <h1 class="text-2xl font-bold text-gray-900">Welcome back</h1>
      <p class="mt-1 text-sm text-gray-500">Log in to your account</p>
    </div>

    <div>
      <label for="email" class="mb-1 block text-sm font-medium text-gray-700">Email</label>
      <input id="email" type="email" required placeholder="you@example.com"
        class="w-full rounded-lg border border-gray-300 px-3 py-2 placeholder:text-gray-400
               focus:border-blue-500 focus:outline-hidden focus:ring-3 focus:ring-blue-500/30" />
    </div>

    <div>
      <div class="mb-1 flex items-center justify-between">
        <label for="password" class="text-sm font-medium text-gray-700">Password</label>
        <a href="#" class="text-sm text-blue-600 hover:underline">Forgot?</a>
      </div>
      <input id="password" type="password" required
        class="w-full rounded-lg border border-gray-300 px-3 py-2
               focus:border-blue-500 focus:outline-hidden focus:ring-3 focus:ring-blue-500/30" />
    </div>

    <label class="flex items-center gap-2 text-sm text-gray-600"><input type="checkbox" class="size-4 rounded accent-blue-600" /> Remember me</label>

    <button class="w-full rounded-lg bg-blue-600 py-2.5 font-semibold text-white transition hover:bg-blue-700 focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2">Log in</button>

    <p class="text-center text-sm text-gray-500">No account? <a href="#" class="font-medium text-blue-600 hover:underline">Sign up</a></p>
  </form>
</div>
```

| Important classes | Why |
|---|---|
| `grid min-h-dvh place-items-center` | centers the form in the viewport |
| `max-w-sm w-full` | fluid on phones, capped on desktop |
| `space-y-5` | consistent vertical rhythm between fields |
| `focus:ring-3 focus:ring-blue-500/30 focus:outline-hidden` | soft visible focus ring replaces the outline |
| `flex justify-between` | label left, link right on one row |

### 31.6 Signup Form

```html
<form class="mx-auto w-full max-w-md space-y-5 rounded-2xl bg-white p-8 shadow-lg">
  <h1 class="text-2xl font-bold text-gray-900">Create your account</h1>

  <div class="grid grid-cols-1 gap-4 sm:grid-cols-2">
    <div>
      <label for="first" class="mb-1 block text-sm font-medium text-gray-700">First name</label>
      <input id="first" class="w-full rounded-lg border border-gray-300 px-3 py-2 focus:border-blue-500 focus:outline-hidden focus:ring-3 focus:ring-blue-500/30" />
    </div>
    <div>
      <label for="last" class="mb-1 block text-sm font-medium text-gray-700">Last name</label>
      <input id="last" class="w-full rounded-lg border border-gray-300 px-3 py-2 focus:border-blue-500 focus:outline-hidden focus:ring-3 focus:ring-blue-500/30" />
    </div>
  </div>

  <div>
    <label for="mail" class="mb-1 block text-sm font-medium text-gray-700">Email</label>
    <input id="mail" type="email" required class="peer w-full rounded-lg border border-gray-300 px-3 py-2
      focus:border-blue-500 focus:outline-hidden focus:ring-3 focus:ring-blue-500/30 user-invalid:border-red-500" />
    <p class="mt-1 hidden text-sm text-red-600 peer-user-invalid:block">Enter a valid email address.</p>
  </div>

  <div>
    <label for="pw" class="mb-1 block text-sm font-medium text-gray-700">Password</label>
    <input id="pw" type="password" minlength="8" required class="w-full rounded-lg border border-gray-300 px-3 py-2 focus:border-blue-500 focus:outline-hidden focus:ring-3 focus:ring-blue-500/30" />
    <p class="mt-1 text-xs text-gray-500">At least 8 characters.</p>
  </div>

  <button class="w-full rounded-lg bg-blue-600 py-2.5 font-semibold text-white hover:bg-blue-700">Sign up</button>
</form>
```

| Important classes | Why |
|---|---|
| `grid grid-cols-1 sm:grid-cols-2 gap-4` | two name fields side by side from 640px |
| `peer` + `peer-user-invalid:block` | error message appears only after the user typed something invalid |
| `user-invalid:border-red-500` | red border after interaction (v4.1+; use `invalid:` on older v4) |

### 31.7 Button Variants

```html
<!-- Primary -->
<button class="rounded-lg bg-blue-600 px-4 py-2 font-medium text-white shadow-sm transition hover:bg-blue-700 active:scale-95 focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2 disabled:opacity-50">Primary</button>

<!-- Secondary -->
<button class="rounded-lg bg-gray-100 px-4 py-2 font-medium text-gray-900 transition hover:bg-gray-200">Secondary</button>

<!-- Outline -->
<button class="rounded-lg border border-blue-600 px-4 py-2 font-medium text-blue-600 transition hover:bg-blue-50">Outline</button>

<!-- Ghost -->
<button class="rounded-lg px-4 py-2 font-medium text-gray-700 transition hover:bg-gray-100">Ghost</button>

<!-- Danger -->
<button class="rounded-lg bg-red-600 px-4 py-2 font-medium text-white transition hover:bg-red-700">Delete</button>

<!-- Gradient -->
<button class="rounded-lg bg-linear-to-r from-indigo-500 to-purple-600 px-5 py-2.5 font-semibold text-white shadow-md transition hover:brightness-110">Gradient</button>

<!-- Pill -->
<button class="rounded-full bg-gray-900 px-6 py-2 text-sm font-medium text-white hover:bg-gray-700">Pill</button>

<!-- Icon only -->
<button class="grid size-10 place-items-center rounded-full hover:bg-gray-100" aria-label="Like"><svg class="size-5">...</svg></button>

<!-- Link style -->
<button class="font-medium text-blue-600 underline-offset-4 hover:underline">Link button</button>

<!-- Sizes: small / medium / large -->
<button class="rounded-md px-3 py-1.5 text-sm">Small</button>
<button class="rounded-lg px-4 py-2 text-base">Medium</button>
<button class="rounded-xl px-6 py-3 text-lg">Large</button>

<!-- Loading -->
<button disabled class="inline-flex items-center gap-2 rounded-lg bg-blue-600 px-4 py-2 text-white opacity-70 cursor-not-allowed">
  <svg class="size-4 animate-spin">...</svg> Saving...
</button>
```

| Important classes | Why |
|---|---|
| `px-4 py-2` | standard button padding (wider than tall) |
| `transition hover:... active:scale-95` | feedback on hover and press |
| `focus-visible:ring-2 ... ring-offset-2` | keyboard focus indicator |
| `disabled:opacity-50` | disabled look |

### 31.8 Modal

```html
<!-- Backdrop -->
<div class="fixed inset-0 z-50 flex items-center justify-center bg-black/50 p-4 backdrop-blur-sm" role="dialog" aria-modal="true" aria-labelledby="modal-title">
  <!-- Panel -->
  <div class="w-full max-w-md rounded-2xl bg-white p-6 shadow-2xl">
    <div class="flex items-start justify-between">
      <h2 id="modal-title" class="text-lg font-semibold text-gray-900">Delete project?</h2>
      <button class="rounded-lg p-1 text-gray-400 hover:bg-gray-100 hover:text-gray-600" aria-label="Close"><svg class="size-5">...</svg></button>
    </div>
    <p class="mt-3 text-sm text-gray-600">This action cannot be undone. All data will be permanently removed.</p>
    <div class="mt-6 flex flex-col-reverse gap-3 sm:flex-row sm:justify-end">
      <button class="rounded-lg border border-gray-300 px-4 py-2 font-medium text-gray-700 hover:bg-gray-50">Cancel</button>
      <button class="rounded-lg bg-red-600 px-4 py-2 font-medium text-white hover:bg-red-700">Delete</button>
    </div>
  </div>
</div>
```

| Important classes | Why |
|---|---|
| `fixed inset-0 z-50` | covers the whole screen above everything |
| `flex items-center justify-center` | centers the panel |
| `bg-black/50 backdrop-blur-sm` | dim and blur the page behind |
| `max-w-md w-full p-4` (outer) | panel never touches screen edges on phones |
| `flex-col-reverse sm:flex-row sm:justify-end` | primary action on top on mobile, right-aligned row on desktop |

In React, render it conditionally: `{open && <Modal onClose={...} />}`. Add `overflow-hidden` to `<body>` while open to stop background scrolling.

### 31.9 Dropdown

```html
<div class="relative inline-block text-left">
  <button class="inline-flex items-center gap-2 rounded-lg border border-gray-300 bg-white px-4 py-2 text-sm font-medium hover:bg-gray-50" aria-expanded="true" aria-haspopup="menu">
    Options <svg class="size-4">...</svg>
  </button>

  <div class="absolute right-0 z-20 mt-2 w-48 origin-top-right rounded-xl border border-gray-200 bg-white p-1 shadow-lg" role="menu">
    <a href="#" class="block rounded-lg px-3 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem">Profile</a>
    <a href="#" class="block rounded-lg px-3 py-2 text-sm text-gray-700 hover:bg-gray-100" role="menuitem">Settings</a>
    <div class="my-1 border-t border-gray-100"></div>
    <a href="#" class="block rounded-lg px-3 py-2 text-sm text-red-600 hover:bg-red-50" role="menuitem">Sign out</a>
  </div>
</div>
```

| Important classes | Why |
|---|---|
| `relative` (wrapper) + `absolute right-0 mt-2` (menu) | menu is anchored under the button |
| `origin-top-right` | scale animations grow from the corner |
| `z-20` | menu sits above surrounding content |
| `block rounded-lg px-3 py-2 hover:bg-gray-100` | large, comfortable click target |

CSS-only hover version: add `group` to the wrapper and use `invisible opacity-0 group-hover:visible group-hover:opacity-100 transition` on the menu. In React, toggle `hidden` with state.

### 31.10 Sidebar

```html
<aside class="flex h-dvh w-64 shrink-0 flex-col border-r border-gray-200 bg-white">
  <div class="flex h-16 items-center px-6 text-xl font-bold text-blue-600">Dashboard</div>

  <nav class="flex-1 space-y-1 overflow-y-auto px-3 py-4">
    <a href="#" class="flex items-center gap-3 rounded-lg bg-blue-50 px-3 py-2 text-sm font-medium text-blue-700"><svg class="size-5">...</svg> Overview</a>
    <a href="#" class="flex items-center gap-3 rounded-lg px-3 py-2 text-sm font-medium text-gray-600 hover:bg-gray-100 hover:text-gray-900"><svg class="size-5">...</svg> Projects</a>
    <a href="#" class="flex items-center gap-3 rounded-lg px-3 py-2 text-sm font-medium text-gray-600 hover:bg-gray-100 hover:text-gray-900"><svg class="size-5">...</svg> Team</a>
  </nav>

  <div class="border-t border-gray-200 p-4">
    <div class="flex items-center gap-3">
      <img class="size-9 rounded-full" src="avatar.jpg" alt="" />
      <div class="min-w-0"><p class="truncate text-sm font-medium">Ada Lovelace</p><p class="truncate text-xs text-gray-500">ada@example.com</p></div>
    </div>
  </div>
</aside>
```

| Important classes | Why |
|---|---|
| `flex h-dvh w-64 shrink-0 flex-col` | fixed-width full-height column that never gets squeezed |
| `flex-1 overflow-y-auto` (nav) | nav fills leftover space and scrolls alone |
| `bg-blue-50 text-blue-700` vs `hover:bg-gray-100` | active versus inactive link styles |
| `min-w-0 truncate` | long emails get an ellipsis inside flex |

Mobile off-canvas version: `fixed inset-y-0 left-0 z-40 -translate-x-full transition-transform lg:static lg:translate-x-0`, and toggle `translate-x-0` in React state.

### 31.11 Dashboard Layout

```html
<div class="flex min-h-dvh bg-gray-100">
  <aside class="hidden w-64 shrink-0 bg-gray-900 text-gray-200 lg:block">Sidebar</aside>

  <div class="flex min-w-0 flex-1 flex-col">
    <header class="sticky top-0 z-10 flex h-16 items-center justify-between border-b bg-white px-6">
      <h1 class="text-lg font-semibold">Overview</h1>
      <img class="size-9 rounded-full" src="avatar.jpg" alt="" />
    </header>

    <main class="flex-1 space-y-6 p-6">
      <!-- stat cards -->
      <div class="grid grid-cols-1 gap-4 sm:grid-cols-2 xl:grid-cols-4">
        <div class="rounded-xl bg-white p-5 shadow-sm">
          <p class="text-sm text-gray-500">Revenue</p>
          <p class="mt-1 text-3xl font-bold tabular-nums">$48,200</p>
          <p class="mt-1 text-sm font-medium text-green-600">+12.5%</p>
        </div>
        <!-- 3 more cards -->
      </div>

      <!-- chart + side panel -->
      <div class="grid gap-6 lg:grid-cols-3">
        <section class="rounded-xl bg-white p-6 shadow-sm lg:col-span-2">Chart</section>
        <section class="rounded-xl bg-white p-6 shadow-sm">Recent activity</section>
      </div>
    </main>
  </div>
</div>
```

| Important classes | Why |
|---|---|
| `flex min-h-dvh` | sidebar + content fill the viewport |
| `min-w-0 flex-1` | content area can shrink; tables cannot blow out the layout |
| `hidden lg:block` | sidebar hidden below 1024px |
| `grid-cols-1 sm:grid-cols-2 xl:grid-cols-4` | stat cards scale 1, 2, 4 columns |
| `lg:col-span-2` | chart takes two thirds on large screens |

### 31.12 Pricing Card

```html
<div class="grid max-w-5xl gap-8 md:grid-cols-3">
  <!-- Regular plan -->
  <div class="flex flex-col rounded-2xl border border-gray-200 bg-white p-8">
    <h3 class="text-lg font-semibold text-gray-900">Starter</h3>
    <p class="mt-4"><span class="text-4xl font-bold tracking-tight">$9</span><span class="text-gray-500">/month</span></p>
    <ul class="mt-6 flex-1 space-y-3 text-sm text-gray-600">
      <li class="flex gap-3"><svg class="size-5 shrink-0 text-green-500">...</svg>1 project</li>
      <li class="flex gap-3"><svg class="size-5 shrink-0 text-green-500">...</svg>Basic analytics</li>
    </ul>
    <button class="mt-8 rounded-lg border border-blue-600 py-2.5 font-semibold text-blue-600 hover:bg-blue-50">Choose Starter</button>
  </div>

  <!-- Highlighted plan -->
  <div class="relative flex flex-col rounded-2xl bg-blue-600 p-8 text-white shadow-xl ring-1 ring-blue-600 md:-translate-y-4">
    <span class="absolute -top-3 left-1/2 -translate-x-1/2 rounded-full bg-amber-400 px-3 py-0.5 text-xs font-bold uppercase text-gray-900">Most popular</span>
    <h3 class="text-lg font-semibold">Pro</h3>
    <p class="mt-4"><span class="text-4xl font-bold tracking-tight">$29</span><span class="text-blue-100">/month</span></p>
    <ul class="mt-6 flex-1 space-y-3 text-sm text-blue-50">
      <li class="flex gap-3"><svg class="size-5 shrink-0">...</svg>Unlimited projects</li>
      <li class="flex gap-3"><svg class="size-5 shrink-0">...</svg>Advanced analytics</li>
    </ul>
    <button class="mt-8 rounded-lg bg-white py-2.5 font-semibold text-blue-600 hover:bg-blue-50">Choose Pro</button>
  </div>
  <!-- Third plan repeats the first style -->
</div>
```

| Important classes | Why |
|---|---|
| `flex flex-col` + `flex-1` on the list | buttons align at the bottom of every card |
| `md:-translate-y-4` | raised highlighted plan on desktop |
| `absolute -top-3 left-1/2 -translate-x-1/2` | ribbon centered on the top edge |
| `shrink-0` on icons | check icons never get squished |

### 31.13 Alert

```html
<!-- Info -->
<div class="flex gap-3 rounded-lg border border-blue-200 bg-blue-50 p-4 text-sm text-blue-800" role="alert">
  <svg class="mt-0.5 size-5 shrink-0">...</svg>
  <div><p class="font-semibold">Heads up</p><p class="mt-1">Your trial ends in 3 days.</p></div>
</div>

<!-- Success -->
<div class="flex gap-3 rounded-lg border border-green-200 bg-green-50 p-4 text-sm text-green-800" role="alert">Saved successfully.</div>

<!-- Warning -->
<div class="flex gap-3 rounded-lg border border-yellow-200 bg-yellow-50 p-4 text-sm text-yellow-800" role="alert">Storage almost full.</div>

<!-- Error -->
<div class="flex gap-3 rounded-lg border border-red-200 bg-red-50 p-4 text-sm text-red-800" role="alert">Payment failed.</div>

<!-- Left accent -->
<div class="rounded-r-lg border-l-4 border-blue-500 bg-blue-50 p-4 text-blue-800">Accent alert</div>
```

Pattern: `bg-{color}-50` + `border-{color}-200` + `text-{color}-800`. Swap the color word for each status.

### 31.14 Badge

```html
<span class="inline-flex items-center rounded-full bg-green-100 px-2.5 py-0.5 text-xs font-medium text-green-800">Active</span>
<span class="inline-flex items-center rounded-full bg-red-100 px-2.5 py-0.5 text-xs font-medium text-red-800">Failed</span>
<span class="inline-flex items-center rounded-md bg-gray-100 px-2 py-1 text-xs font-medium text-gray-600 ring-1 ring-inset ring-gray-500/10">Draft</span>

<!-- With dot -->
<span class="inline-flex items-center gap-1.5 rounded-full bg-emerald-50 px-2.5 py-1 text-xs font-medium text-emerald-700">
  <span class="size-1.5 rounded-full bg-emerald-500"></span> Online
</span>

<!-- Notification count on an icon -->
<div class="relative inline-block">
  <svg class="size-6">...</svg>
  <span class="absolute -right-1 -top-1 grid size-4 place-items-center rounded-full bg-red-500 text-[10px] font-bold text-white">3</span>
</div>
```

### 31.15 Loading Spinner

```html
<!-- Border spinner -->
<div class="size-8 animate-spin rounded-full border-4 border-gray-200 border-t-blue-600" role="status" aria-label="Loading"></div>

<!-- SVG spinner (inherits text color) -->
<svg class="size-6 animate-spin text-blue-600" viewBox="0 0 24 24" fill="none" role="status" aria-label="Loading">
  <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4" />
  <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z" />
</svg>

<!-- Full-page loader -->
<div class="fixed inset-0 grid place-items-center bg-white/70 backdrop-blur-sm">
  <div class="size-10 animate-spin rounded-full border-4 border-blue-200 border-t-blue-600"></div>
</div>

<!-- Bouncing dots -->
<div class="flex gap-1">
  <span class="size-2 animate-bounce rounded-full bg-blue-600 [animation-delay:-0.3s]"></span>
  <span class="size-2 animate-bounce rounded-full bg-blue-600 [animation-delay:-0.15s]"></span>
  <span class="size-2 animate-bounce rounded-full bg-blue-600"></span>
</div>
```

The border trick: a gray border all around, and a **colored top border** (`border-t-blue-600`) that spins.

### 31.16 Skeleton Loader

```html
<div class="w-full max-w-sm animate-pulse rounded-xl border border-gray-200 p-4">
  <div class="h-40 rounded-lg bg-gray-200"></div>
  <div class="mt-4 space-y-3">
    <div class="h-4 w-3/4 rounded bg-gray-200"></div>
    <div class="h-4 rounded bg-gray-200"></div>
    <div class="h-4 w-5/6 rounded bg-gray-200"></div>
  </div>
  <div class="mt-4 flex items-center gap-3">
    <div class="size-10 rounded-full bg-gray-200"></div>
    <div class="h-3 w-24 rounded bg-gray-200"></div>
  </div>
</div>
```

`animate-pulse` on the parent fades every gray block together. Match block sizes to the real content to prevent layout shift. In React: `{loading ? <Skeleton /> : <Card />}`.

### 31.17 Image Gallery

```html
<!-- Uniform grid -->
<div class="grid grid-cols-2 gap-3 md:grid-cols-3 lg:grid-cols-4">
  <div class="group overflow-hidden rounded-xl bg-gray-100">
    <img class="aspect-square size-full object-cover transition duration-300 group-hover:scale-110" src="1.jpg" alt="" />
  </div>
  <!-- repeat -->
</div>

<!-- Masonry-style using CSS columns -->
<div class="columns-2 gap-3 md:columns-3 lg:columns-4">
  <img class="mb-3 w-full break-inside-avoid rounded-xl" src="a.jpg" alt="" />
  <img class="mb-3 w-full break-inside-avoid rounded-xl" src="b.jpg" alt="" />
</div>

<!-- Featured image spanning cells -->
<div class="grid grid-cols-3 gap-3">
  <img class="col-span-2 row-span-2 size-full rounded-xl object-cover" src="big.jpg" alt="" />
  <img class="aspect-square w-full rounded-xl object-cover" src="s1.jpg" alt="" />
  <img class="aspect-square w-full rounded-xl object-cover" src="s2.jpg" alt="" />
</div>

<!-- Overlay caption on hover -->
<div class="group relative overflow-hidden rounded-xl">
  <img class="aspect-4/3 w-full object-cover" src="p.jpg" alt="" />
  <div class="absolute inset-0 flex items-end bg-linear-to-t from-black/70 to-transparent p-4 opacity-0 transition-opacity group-hover:opacity-100">
    <p class="font-medium text-white">Caption</p>
  </div>
</div>
```

### 31.18 Responsive Grid

```html
<!-- Fixed breakpoints -->
<div class="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4">
  <article class="rounded-xl border border-gray-200 bg-white p-6 shadow-sm">...</article>
</div>

<!-- Auto-fit (no breakpoints) -->
<div class="grid grid-cols-[repeat(auto-fit,minmax(16rem,1fr))] gap-6">...</div>

<!-- Container-query version: reacts to the parent's width -->
<div class="@container">
  <div class="grid grid-cols-1 gap-4 @md:grid-cols-2 @3xl:grid-cols-4">...</div>
</div>
```

### 31.19 Footer

```html
<footer class="bg-gray-900 text-gray-400">
  <div class="mx-auto max-w-7xl px-4 py-12 sm:px-6 lg:px-8">
    <div class="grid grid-cols-2 gap-8 md:grid-cols-4">
      <div class="col-span-2 md:col-span-1">
        <p class="text-xl font-bold text-white">Brand</p>
        <p class="mt-3 text-sm">Short company description goes here.</p>
      </div>
      <div>
        <h4 class="text-sm font-semibold uppercase tracking-wider text-white">Product</h4>
        <ul class="mt-4 space-y-2 text-sm">
          <li><a href="#" class="transition-colors hover:text-white">Features</a></li>
          <li><a href="#" class="transition-colors hover:text-white">Pricing</a></li>
        </ul>
      </div>
      <div>
        <h4 class="text-sm font-semibold uppercase tracking-wider text-white">Company</h4>
        <ul class="mt-4 space-y-2 text-sm">
          <li><a href="#" class="transition-colors hover:text-white">About</a></li>
          <li><a href="#" class="transition-colors hover:text-white">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4 class="text-sm font-semibold uppercase tracking-wider text-white">Legal</h4>
        <ul class="mt-4 space-y-2 text-sm">
          <li><a href="#" class="transition-colors hover:text-white">Privacy</a></li>
          <li><a href="#" class="transition-colors hover:text-white">Terms</a></li>
        </ul>
      </div>
    </div>
    <div class="mt-10 flex flex-col items-center justify-between gap-4 border-t border-gray-800 pt-8 text-sm sm:flex-row">
      <p>&copy; 2026 Brand. All rights reserved.</p>
      <div class="flex gap-4"><a href="#" class="hover:text-white">Twitter</a><a href="#" class="hover:text-white">GitHub</a></div>
    </div>
  </div>
</footer>
```

| Important classes | Why |
|---|---|
| `grid-cols-2 md:grid-cols-4` + `col-span-2 md:col-span-1` | brand block spans the full width on mobile |
| `text-gray-400 hover:text-white` | muted links that brighten on hover |
| `flex-col sm:flex-row justify-between` | copyright and socials stack on mobile |
| `border-t border-gray-800` | subtle divider on dark background |


---


## 32. CSS → Tailwind Conversion Table

Find the CSS you know, read the Tailwind class on the right. `n` means "a number from the spacing scale" (n x 4px).

### 32.1 Display and Layout

| CSS | Tailwind | Notes |
|---|---|---|
| `display: block` | `block` | |
| `display: inline` | `inline` | |
| `display: inline-block` | `inline-block` | |
| `display: flex` | `flex` | |
| `display: inline-flex` | `inline-flex` | |
| `display: grid` | `grid` | |
| `display: inline-grid` | `inline-grid` | |
| `display: none` | `hidden` | |
| `display: contents` | `contents` | |
| `display: table` | `table` | also `table-row`, `table-cell` |
| `display: flow-root` | `flow-root` | |
| `visibility: hidden` | `invisible` | keeps space |
| `visibility: visible` | `visible` | |
| `float: left` / `right` / `none` | `float-left` / `float-right` / `float-none` | |
| `clear: both` | `clear-both` | |
| `box-sizing: border-box` | `box-border` | default in Tailwind |
| `box-sizing: content-box` | `box-content` | |
| `columns: 3` | `columns-3` | |
| `isolation: isolate` | `isolate` | |

### 32.2 Spacing and Sizing

| CSS | Tailwind | Notes |
|---|---|---|
| `margin: 1rem` | `m-4` | |
| `margin: 0 auto` | `mx-auto` | center a block |
| `margin: 0 1rem` | `mx-4` | |
| `margin: 1rem 0` | `my-4` | |
| `margin-top: 1.5rem` | `mt-6` | |
| `margin-right: 0.5rem` | `mr-2` | |
| `margin-bottom: 2rem` | `mb-8` | |
| `margin-left: auto` | `ml-auto` | push right |
| `margin: -1rem` | `-m-4` | negative |
| `padding: 1rem` | `p-4` | |
| `padding: 0.5rem 1rem` | `py-2 px-4` | |
| `padding-top: 1rem` | `pt-4` | |
| `padding-left: 2rem` | `pl-8` | |
| `gap: 1rem` | `gap-4` | flex/grid |
| `column-gap: 1.5rem` | `gap-x-6` | |
| `row-gap: 0.5rem` | `gap-y-2` | |
| `width: 100%` | `w-full` | |
| `width: 50%` | `w-1/2` | |
| `width: 100vw` | `w-screen` | |
| `width: auto` | `w-auto` | |
| `width: fit-content` | `w-fit` | |
| `width: 16rem` | `w-64` | |
| `width: 350px` | `w-[350px]` | arbitrary |
| `height: 100%` | `h-full` | |
| `height: 100vh` | `h-screen` | |
| `height: 100dvh` | `h-dvh` | |
| `height: 3rem` | `h-12` | |
| `width: 2.5rem; height: 2.5rem` | `size-10` | |
| `min-width: 0` | `min-w-0` | |
| `max-width: 28rem` | `max-w-md` | |
| `max-width: 80rem` | `max-w-7xl` | |
| `max-width: 100%` | `max-w-full` | |
| `min-height: 100vh` | `min-h-screen` | |
| `max-height: 24rem` | `max-h-96` | |
| `aspect-ratio: 16 / 9` | `aspect-video` | |
| `aspect-ratio: 1 / 1` | `aspect-square` | |

### 32.3 Flexbox

| CSS | Tailwind | Notes |
|---|---|---|
| `flex-direction: row` | `flex-row` | default |
| `flex-direction: column` | `flex-col` | |
| `flex-direction: row-reverse` | `flex-row-reverse` | |
| `flex-wrap: wrap` | `flex-wrap` | |
| `flex-wrap: nowrap` | `flex-nowrap` | |
| `justify-content: flex-start` | `justify-start` | |
| `justify-content: center` | `justify-center` | |
| `justify-content: flex-end` | `justify-end` | |
| `justify-content: space-between` | `justify-between` | |
| `justify-content: space-around` | `justify-around` | |
| `justify-content: space-evenly` | `justify-evenly` | |
| `align-items: flex-start` | `items-start` | |
| `align-items: center` | `items-center` | |
| `align-items: flex-end` | `items-end` | |
| `align-items: baseline` | `items-baseline` | |
| `align-items: stretch` | `items-stretch` | |
| `align-content: center` | `content-center` | |
| `align-self: center` | `self-center` | |
| `align-self: flex-end` | `self-end` | |
| `flex: 1 1 0%` | `flex-1` | |
| `flex: 1 1 auto` | `flex-auto` | |
| `flex: 0 1 auto` | `flex-initial` | |
| `flex: none` | `flex-none` | |
| `flex-grow: 1` | `grow` | |
| `flex-grow: 0` | `grow-0` | |
| `flex-shrink: 0` | `shrink-0` | |
| `flex-basis: 50%` | `basis-1/2` | |
| `order: 1` | `order-1` | |
| `order: -9999` | `order-first` | |

### 32.4 Grid

| CSS | Tailwind | Notes |
|---|---|---|
| `grid-template-columns: repeat(3, minmax(0, 1fr))` | `grid-cols-3` | |
| `grid-template-columns: 200px 1fr` | `grid-cols-[200px_1fr]` | arbitrary |
| `grid-template-rows: repeat(2, minmax(0, 1fr))` | `grid-rows-2` | |
| `grid-column: span 2 / span 2` | `col-span-2` | |
| `grid-column: 1 / -1` | `col-span-full` | |
| `grid-column-start: 2` | `col-start-2` | |
| `grid-row: span 2 / span 2` | `row-span-2` | |
| `grid-auto-flow: column` | `grid-flow-col` | |
| `grid-auto-rows: min-content` | `auto-rows-min` | |
| `justify-items: center` | `justify-items-center` | |
| `place-items: center` | `place-items-center` | |
| `place-content: center` | `place-content-center` | |
| `place-self: center` | `place-self-center` | |

### 32.5 Position

| CSS | Tailwind | Notes |
|---|---|---|
| `position: static` | `static` | |
| `position: relative` | `relative` | |
| `position: absolute` | `absolute` | |
| `position: fixed` | `fixed` | |
| `position: sticky` | `sticky` | |
| `top: 0` | `top-0` | |
| `right: 0` | `right-0` | |
| `bottom: 1rem` | `bottom-4` | |
| `left: 50%` | `left-1/2` | |
| `top: 0; right: 0; bottom: 0; left: 0` | `inset-0` | |
| `left: 0; right: 0` | `inset-x-0` | |
| `top: 0; bottom: 0` | `inset-y-0` | |
| `top: -0.5rem` | `-top-2` | |
| `z-index: 10` | `z-10` | |
| `z-index: 9999` | `z-[9999]` | |

### 32.6 Typography

| CSS | Tailwind | Notes |
|---|---|---|
| `font-family: sans-serif` | `font-sans` | |
| `font-family: serif` | `font-serif` | |
| `font-family: monospace` | `font-mono` | |
| `font-size: 0.875rem` | `text-sm` | |
| `font-size: 1rem` | `text-base` | |
| `font-size: 1.25rem` | `text-xl` | |
| `font-size: 1.5rem` | `text-2xl` | |
| `font-size: 24px` | `text-2xl` | (1.5rem) |
| `font-size: 22px` | `text-[22px]` | arbitrary |
| `font-weight: 300` | `font-light` | |
| `font-weight: 400` | `font-normal` | |
| `font-weight: 500` | `font-medium` | |
| `font-weight: 600` | `font-semibold` | |
| `font-weight: 700` | `font-bold` | |
| `font-weight: 900` | `font-black` | |
| `font-style: italic` | `italic` | |
| `font-style: normal` | `not-italic` | |
| `line-height: 1` | `leading-none` | |
| `line-height: 1.25` | `leading-tight` | |
| `line-height: 1.5` | `leading-normal` | |
| `line-height: 1.625` | `leading-relaxed` | |
| `line-height: 2rem` | `leading-8` | |
| `letter-spacing: -0.025em` | `tracking-tight` | |
| `letter-spacing: 0.05em` | `tracking-wider` | |
| `text-align: left` / `center` / `right` / `justify` | `text-left` / `text-center` / `text-right` / `text-justify` | |
| `text-transform: uppercase` | `uppercase` | |
| `text-transform: capitalize` | `capitalize` | |
| `text-transform: none` | `normal-case` | |
| `text-decoration: underline` | `underline` | |
| `text-decoration: line-through` | `line-through` | |
| `text-decoration: none` | `no-underline` | |
| `text-underline-offset: 4px` | `underline-offset-4` | |
| `text-overflow: ellipsis` | `text-ellipsis` | |
| `overflow: hidden; text-overflow: ellipsis; white-space: nowrap` | `truncate` | |
| `white-space: nowrap` | `whitespace-nowrap` | |
| `white-space: pre-wrap` | `whitespace-pre-wrap` | |
| `word-break: break-all` | `break-all` | |
| `overflow-wrap: break-word` | `break-words` | |
| `text-wrap: balance` | `text-balance` | |
| `vertical-align: middle` | `align-middle` | |
| `text-indent: 1rem` | `indent-4` | |
| `font-variant-numeric: tabular-nums` | `tabular-nums` | |
| `-webkit-line-clamp: 3` | `line-clamp-3` | |
| `list-style-type: disc` | `list-disc` | |
| `list-style-type: none` | `list-none` | |

### 32.7 Colors and Backgrounds

| CSS | Tailwind | Notes |
|---|---|---|
| `color: #3b82f6` | `text-blue-500` | |
| `color: white` | `text-white` | |
| `color: rgb(0 0 0 / 0.5)` | `text-black/50` | |
| `color: #1e293b` | `text-[#1e293b]` | arbitrary |
| `color: currentColor` | `text-current` | |
| `background-color: #3b82f6` | `bg-blue-500` | |
| `background-color: transparent` | `bg-transparent` | |
| `background-color: rgb(0 0 0 / 0.5)` | `bg-black/50` | |
| `background-image: url(...)` | `bg-[url(/img.jpg)]` | |
| `background-image: none` | `bg-none` | |
| `background-image: linear-gradient(to right, a, b)` | `bg-linear-to-r from-a to-b` | |
| `background-size: cover` | `bg-cover` | |
| `background-size: contain` | `bg-contain` | |
| `background-position: center` | `bg-center` | |
| `background-repeat: no-repeat` | `bg-no-repeat` | |
| `background-attachment: fixed` | `bg-fixed` | |
| `background-clip: text` | `bg-clip-text` | |
| `opacity: 0.5` | `opacity-50` | |
| `accent-color: #3b82f6` | `accent-blue-500` | |
| `caret-color: #3b82f6` | `caret-blue-500` | |
| `fill: currentColor` | `fill-current` | |
| `stroke: currentColor` | `stroke-current` | |
| `mix-blend-mode: multiply` | `mix-blend-multiply` | |

### 32.8 Borders, Radius, Shadows

| CSS | Tailwind | Notes |
|---|---|---|
| `border: 1px solid` | `border` | add a color |
| `border: 2px solid #e5e7eb` | `border-2 border-gray-200` | |
| `border-width: 0` | `border-0` | |
| `border-top: 1px solid` | `border-t` | |
| `border-bottom: 2px solid` | `border-b-2` | |
| `border-left: 4px solid` | `border-l-4` | |
| `border-left-width + border-right-width` | `border-x` | |
| `border-color: #e5e7eb` | `border-gray-200` | |
| `border-style: dashed` | `border-dashed` | |
| `border-style: dotted` | `border-dotted` | |
| `border-radius: 4px` | `rounded-sm` | |
| `border-radius: 6px` | `rounded-md` | |
| `border-radius: 8px` | `rounded-lg` | |
| `border-radius: 12px` | `rounded-xl` | |
| `border-radius: 16px` | `rounded-2xl` | |
| `border-radius: 9999px` | `rounded-full` | |
| `border-radius: 50%` | `rounded-full` | circle |
| `border-radius: 0` | `rounded-none` | |
| `border-top-left-radius: 8px` | `rounded-tl-lg` | |
| `border-radius: 10px 10px 0 0` | `rounded-t-[10px]` | |
| `border-collapse: collapse` | `border-collapse` | |
| `outline: none` | `outline-none` | or `outline-hidden` |
| `outline: 2px solid blue` | `outline-2 outline-blue-500` | |
| `outline-offset: 2px` | `outline-offset-2` | |
| `box-shadow: 0 1px 2px rgb(0 0 0 / 0.05)` | `shadow-xs` | |
| `box-shadow: 0 1px 3px rgb(0 0 0 / 0.1)...` | `shadow-sm` | |
| `box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1)...` | `shadow-md` | |
| `box-shadow: 0 10px 15px -3px rgb(0 0 0 / 0.1)...` | `shadow-lg` | |
| `box-shadow: 0 20px 25px -5px rgb(0 0 0 / 0.1)...` | `shadow-xl` | |
| `box-shadow: 0 25px 50px -12px rgb(0 0 0 / 0.25)` | `shadow-2xl` | |
| `box-shadow: none` | `shadow-none` | |
| `box-shadow: 0 4px 20px rgba(0,0,0,.15)` | `shadow-[0_4px_20px_rgba(0,0,0,0.15)]` | |
| `box-shadow: inset 0 2px 4px ...` | `inset-shadow-sm` | |
| `box-shadow: 0 0 0 3px blue` (focus ring) | `ring-3 ring-blue-500` | |

### 32.9 Overflow, Objects, Interactivity

| CSS | Tailwind | Notes |
|---|---|---|
| `overflow: hidden` | `overflow-hidden` | |
| `overflow: auto` | `overflow-auto` | |
| `overflow: scroll` | `overflow-scroll` | |
| `overflow-x: auto` | `overflow-x-auto` | |
| `overflow-y: scroll` | `overflow-y-scroll` | |
| `overscroll-behavior: contain` | `overscroll-contain` | |
| `object-fit: cover` | `object-cover` | |
| `object-fit: contain` | `object-contain` | |
| `object-position: top` | `object-top` | |
| `cursor: pointer` | `cursor-pointer` | |
| `cursor: not-allowed` | `cursor-not-allowed` | |
| `cursor: grab` | `cursor-grab` | |
| `pointer-events: none` | `pointer-events-none` | |
| `user-select: none` | `select-none` | |
| `resize: none` | `resize-none` | |
| `appearance: none` | `appearance-none` | |
| `scroll-behavior: smooth` | `scroll-smooth` | |
| `scroll-snap-type: x mandatory` | `snap-x snap-mandatory` | |
| `scroll-snap-align: start` | `snap-start` | |
| `touch-action: none` | `touch-none` | |
| `will-change: transform` | `will-change-transform` | |
| `field-sizing: content` | `field-sizing-content` | |

### 32.10 Transitions, Transforms, Filters

| CSS | Tailwind | Notes |
|---|---|---|
| `transition: all 150ms` | `transition-all` | |
| `transition-property: color, background-color...` | `transition-colors` | |
| `transition-property: opacity` | `transition-opacity` | |
| `transition-property: transform` | `transition-transform` | |
| `transition-duration: 300ms` | `duration-300` | |
| `transition-timing-function: ease-in-out` | `ease-in-out` | |
| `transition-delay: 100ms` | `delay-100` | |
| `animation: spin 1s linear infinite` | `animate-spin` | |
| `animation: pulse 2s ...` | `animate-pulse` | |
| `animation: none` | `animate-none` | |
| `transform: scale(1.05)` | `scale-105` | |
| `transform: scaleX(-1)` | `-scale-x-100` | |
| `transform: rotate(45deg)` | `rotate-45` | |
| `transform: rotate(-12deg)` | `-rotate-12` | |
| `transform: translateX(1rem)` | `translate-x-4` | |
| `transform: translateY(-4px)` | `-translate-y-1` | |
| `transform: translate(-50%, -50%)` | `-translate-x-1/2 -translate-y-1/2` | |
| `transform: skewX(12deg)` | `skew-x-12` | |
| `transform-origin: top left` | `origin-top-left` | |
| `filter: blur(8px)` | `blur-sm` | |
| `filter: brightness(1.1)` | `brightness-110` | |
| `filter: grayscale(100%)` | `grayscale` | |
| `filter: invert(100%)` | `invert` | |
| `filter: drop-shadow(...)` | `drop-shadow-md` | |
| `backdrop-filter: blur(12px)` | `backdrop-blur-md` | |
| `backdrop-filter: brightness(0.5)` | `backdrop-brightness-50` | |

### 32.11 Media Queries and Pseudo-classes

| CSS | Tailwind | Notes |
|---|---|---|
| `@media (min-width: 640px)` | `sm:` | |
| `@media (min-width: 768px)` | `md:` | |
| `@media (min-width: 1024px)` | `lg:` | |
| `@media (min-width: 1280px)` | `xl:` | |
| `@media (max-width: 767px)` | `max-md:` | |
| `@media (min-width: 900px)` | `min-[900px]:` | |
| `@media (prefers-color-scheme: dark)` | `dark:` | |
| `@media (prefers-reduced-motion: reduce)` | `motion-reduce:` | |
| `@media print` | `print:` | |
| `@container (min-width: 28rem)` | `@md:` | |
| `:hover` | `hover:` | |
| `:focus` | `focus:` | |
| `:focus-visible` | `focus-visible:` | |
| `:active` | `active:` | |
| `:disabled` | `disabled:` | |
| `:checked` | `checked:` | |
| `:first-child` | `first:` | |
| `:last-child` | `last:` | |
| `:nth-child(odd)` | `odd:` | |
| `:nth-child(even)` | `even:` | |
| `::before` | `before:` | |
| `::after` | `after:` | |
| `::placeholder` | `placeholder:` | |
| `::selection` | `selection:` | |
| `content: ''` | `content-['']` | |
| `:has(...)` | `has-[...]:` | |
| `:not(...)` | `not-*:` | |


---

## 33. "I Want To Do X" Quick Finder

Search this section with Ctrl+F using the words you think in ("center", "hide", "round", "shadow"...).

### 33.1 Layout

| I want to... | Use |
|---|---|
| I want to center something (horizontally and vertically) | `flex items-center justify-center` |
| I want to center with grid | `grid place-items-center` |
| I want to center a block horizontally | `mx-auto` (with a width, e.g. `max-w-md`) |
| I want to center text | `text-center` |
| I want to center absolutely | `absolute top-1/2 left-1/2 -translate-x-1/2 -translate-y-1/2` |
| I want a full-screen section | `min-h-screen` (mobile friendly: `min-h-dvh`) |
| I want a full-width element | `w-full` |
| I want a centered page container | `mx-auto max-w-7xl px-4 sm:px-6 lg:px-8` |
| I want two items on opposite sides | `flex justify-between items-center` |
| I want items in a row with space | `flex gap-4` |
| I want items stacked with space | `flex flex-col gap-4` or `space-y-4` |
| I want to push one item to the far right | `ml-auto` |
| I want items to wrap to the next line | `flex flex-wrap gap-2` |
| I want equal-width columns | `flex` + `flex-1` on children, or `grid grid-cols-3` |
| I want a sidebar and main content | `flex` + `w-64 shrink-0` and `flex-1 min-w-0` |
| I want a sticky footer | `flex min-h-screen flex-col` + `flex-1` on main |
| I want a 3-column responsive layout | `grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6` |
| I want a 12-column grid | `grid grid-cols-12 gap-4` + `col-span-*` |
| I want cards that auto-fill the width | `grid grid-cols-[repeat(auto-fit,minmax(250px,1fr))] gap-6` |
| I want a stack on mobile and a row on desktop | `flex flex-col md:flex-row` |
| I want to overlap elements | `relative` parent + `absolute` child, or negative margin `-mt-8` |
| I want to cover the parent completely | `absolute inset-0` |
| I want an element fixed to the screen corner | `fixed bottom-4 right-4` |
| I want a sticky header | `sticky top-0 z-10` |
| I want to put one thing on top of another | `relative z-10` / `z-20` |
| I want to make a square | `aspect-square` or `size-24` |
| I want a 16:9 box | `aspect-video` |
| I want to reverse the order on mobile | `flex flex-col-reverse` or `order-*` |

### 33.2 Visibility and Responsive

| I want to... | Use |
|---|---|
| I want to hide an element | `hidden` |
| I want to hide on mobile, show on desktop | `hidden md:block` (or `hidden md:flex`) |
| I want to show on mobile only | `md:hidden` |
| I want to hide but keep the space | `invisible` |
| I want to hide visually but keep for screen readers | `sr-only` |
| I want to change size by screen width | `text-sm md:text-lg lg:text-2xl` |
| I want smaller padding on mobile | `p-4 md:p-8` |
| I want to style only between tablet and laptop | `md:max-lg:...` |
| I want a different layout based on the parent's width | `@container` on the parent + `@md:...` on children |
| I want to hide when printing | `print:hidden` |

### 33.3 Shape, Borders, Shadows

| I want to... | Use |
|---|---|
| I want a circular image | `rounded-full object-cover size-24` |
| I want rounded corners | `rounded-lg` (or `rounded-xl`, `rounded-2xl`) |
| I want a pill-shaped button | `rounded-full px-6 py-2` |
| I want only top corners rounded | `rounded-t-lg` |
| I want a shadow card | `rounded-xl shadow-lg` |
| I want a subtle shadow | `shadow-sm` |
| I want a bigger shadow on hover | `shadow-md hover:shadow-xl transition-shadow` |
| I want a colored glow | `shadow-lg shadow-blue-500/50` |
| I want a border | `border border-gray-200` |
| I want a dashed border | `border-2 border-dashed border-gray-300` |
| I want a line between list items | `divide-y divide-gray-200` |
| I want a bottom border only | `border-b border-gray-200` |
| I want a left accent bar | `border-l-4 border-blue-500` |
| I want a focus ring | `focus:ring-2 focus:ring-blue-500` |
| I want to remove the outline accessibly | `outline-hidden` (add a ring on `focus-visible:`) |
| I want an inner shadow | `inset-shadow-sm` |

### 33.4 Color and Background

| I want to... | Use |
|---|---|
| I want a blue button | `bg-blue-600 text-white hover:bg-blue-700` |
| I want muted gray text | `text-gray-500` |
| I want a semi-transparent black overlay | `bg-black/50` |
| I want a gradient background | `bg-linear-to-r from-indigo-500 to-purple-600` |
| I want gradient text | `bg-linear-to-r from-blue-500 to-pink-500 bg-clip-text text-transparent` |
| I want a background image that covers | `bg-[url(/img.jpg)] bg-cover bg-center` |
| I want a fade-to-dark image overlay | `bg-linear-to-t from-black/70 to-transparent` |
| I want a frosted glass effect | `bg-white/20 backdrop-blur-lg border border-white/30` |
| I want a custom hex color | `bg-[#1e293b]` |
| I want dark mode colors | `bg-white dark:bg-gray-900 text-gray-900 dark:text-white` |
| I want an icon to match text color | `fill-current` or `stroke-current` |
| I want to color a checkbox | `accent-blue-600` |
| I want to color the typing cursor | `caret-blue-500` |
| I want a faded (disabled) element | `opacity-50 cursor-not-allowed` |
| I want a transparent background | `bg-transparent` |

### 33.5 Text

| I want to... | Use |
|---|---|
| I want a big bold heading | `text-4xl font-bold tracking-tight` |
| I want small gray caption text | `text-sm text-gray-500` |
| I want uppercase small labels | `text-xs font-semibold uppercase tracking-wider` |
| I want comfortable paragraph text | `text-base leading-relaxed text-gray-600` |
| I want a readable line length | `max-w-prose` (or `max-w-2xl`) |
| I want one line with an ellipsis | `truncate` |
| I want to show only 3 lines | `line-clamp-3` |
| I want text not to wrap | `whitespace-nowrap` |
| I want to break long words/URLs | `break-words` or `break-all` |
| I want balanced headline wrapping | `text-balance` |
| I want to underline only on hover | `no-underline hover:underline` |
| I want a link look | `text-blue-600 underline underline-offset-4 hover:text-blue-800` |
| I want strikethrough | `line-through` |
| I want monospace code | `font-mono text-sm` |
| I want numbers that align in columns | `tabular-nums` |
| I want a drop cap | `first-letter:text-5xl first-letter:font-bold first-letter:float-left` |
| I want to keep line breaks from a textarea | `whitespace-pre-line` |
| I want to disable text selection | `select-none` |

### 33.6 Interaction and Animation

| I want to... | Use |
|---|---|
| I want a hover animation | `transition hover:scale-105` |
| I want a hover lift | `transition hover:-translate-y-1 hover:shadow-lg` |
| I want a smooth color change on hover | `transition-colors duration-200 hover:bg-blue-600` |
| I want a press effect | `active:scale-95 transition` |
| I want a spinner | `animate-spin rounded-full border-4 border-gray-200 border-t-blue-600 size-8` |
| I want a skeleton loading effect | `animate-pulse bg-gray-200 rounded` |
| I want a pulsing notification dot | `animate-ping` on an absolute ring + a solid dot |
| I want a bouncing arrow | `animate-bounce` |
| I want a pointer cursor | `cursor-pointer` |
| I want a forbidden cursor | `cursor-not-allowed` |
| I want clicks to pass through an overlay | `pointer-events-none` |
| I want smooth scrolling for anchors | `scroll-smooth` on `<html>` |
| I want horizontal scroll with snapping | `flex overflow-x-auto snap-x snap-mandatory` + `snap-start shrink-0` |
| I want to show a child when the parent is hovered | `group` on parent + `group-hover:opacity-100` on child |
| I want to react to a sibling's state | `peer` on the earlier sibling + `peer-checked:...` |
| I want to style when a checkbox is checked | `checked:bg-blue-600` or `peer-checked:` |
| I want to respect reduced motion | `motion-safe:animate-spin motion-reduce:animate-none` |
| I want a fade-in when mounted | `transition-opacity starting:opacity-0` |
| I want a custom animation | define `--animate-name` in `@theme`, then `animate-name` |

### 33.7 Images, Forms, Misc

| I want to... | Use |
|---|---|
| I want an image to fill its box without distortion | `size-full object-cover` |
| I want an image to fit without cropping | `object-contain` |
| I want a responsive image | `max-w-full h-auto` |
| I want to zoom an image on hover | `overflow-hidden` wrapper + `transition hover:scale-110` on img |
| I want a grayscale image that gets color on hover | `grayscale hover:grayscale-0 transition` |
| I want to blur a background | `backdrop-blur-md` |
| I want an input that looks good | `rounded-lg border border-gray-300 px-3 py-2 focus:ring-3 focus:ring-blue-500/30 focus:outline-hidden focus:border-blue-500` |
| I want styled placeholder text | `placeholder:text-gray-400` |
| I want an input error state | `invalid:border-red-500` or `user-invalid:border-red-500` |
| I want a disabled input look | `disabled:bg-gray-100 disabled:cursor-not-allowed` |
| I want a textarea that cannot be resized | `resize-none` |
| I want a textarea that grows with content | `field-sizing-content` |
| I want a custom file button | `file:rounded-full file:bg-blue-50 file:px-4 file:py-2` |
| I want to space list items evenly | `space-y-2` |
| I want bullets back on a list | `list-disc pl-5` |
| I want a scrollable box | `max-h-64 overflow-y-auto` |
| I want a scrollable table on mobile | wrapper `overflow-x-auto` |
| I want a custom value that is not in Tailwind | `w-[350px]`, `mt-[37px]`, `bg-[#123456]` |
| I want to override with !important | `text-red-500!` |
| I want to style direct children | `*:p-2` or `[&>li]:py-2` |
| I want to add content with ::before | `before:content-[''] before:absolute` |
| I want to style based on a data attribute | `data-[state=open]:bg-blue-50` |

---

## 34. Class Name Construction Guide

### 34.1 The Recipe

```text
1. Which CSS property?        font-size
2. What is Tailwind's prefix? text
3. What value?                24px  -> closest scale step 2xl (1.5rem = 24px)
4. Join them:                 text-2xl
```

If no scale value matches: `text-[22px]`.

### 34.2 Worked Example: Heading

```css
font-size: 24px;
font-weight: 700;
color: blue;
```

```text
text-2xl font-bold text-blue-500
```

- `font-size: 24px`: property `font-size` uses prefix `text`. 24px is `1.5rem`, and the `2xl` step is 1.5rem. So `text-2xl`.
- `font-weight: 700`: prefix `font`; 700 is named `bold`. So `font-bold`.
- `color: blue`: prefix `text` (the same prefix as size, Tailwind tells them apart by value); pick a hue and shade. `blue` + `500`. So `text-blue-500`.

### 34.3 Worked Example: Card

```css
background: white;
padding: 24px;
border-radius: 12px;
box-shadow: 0 10px 15px rgba(0,0,0,.1);
border: 1px solid #e5e7eb;
```

```text
bg-white p-6 rounded-xl shadow-lg border border-gray-200
```

- `padding: 24px`: prefix `p`; 24 / 4 = 6. So `p-6`.
- `border-radius: 12px`: prefix `rounded`; 12px is the `xl` step. So `rounded-xl`.
- `box-shadow`: prefix `shadow`; a large soft shadow is `lg`. So `shadow-lg`.
- `border: 1px solid #e5e7eb`: `border` gives 1px solid; `#e5e7eb` is `gray-200`. So `border border-gray-200`.

### 34.4 Worked Example: Centered Flex Row

```css
display: flex;
justify-content: space-between;
align-items: center;
gap: 16px;
```

```text
flex justify-between items-center gap-4
```

- `display: flex` becomes `flex`.
- `justify-content: space-between`: the property abbreviates to `justify`, the value `space-between` to `between`. So `justify-between`.
- `align-items: center`: `align-items` abbreviates to `items`. So `items-center`.
- `gap: 16px`: 16 / 4 = 4. So `gap-4`.

### 34.5 Worked Example: Button

```css
background-color: #2563eb;
color: white;
padding: 8px 16px;
border-radius: 8px;
font-weight: 500;
transition: background-color 200ms;
/* hover */ background-color: #1d4ed8;
```

```text
bg-blue-600 text-white px-4 py-2 rounded-lg font-medium transition-colors duration-200 hover:bg-blue-700
```

- `#2563eb` is `blue-600`; `#1d4ed8` is `blue-700`.
- `padding: 8px 16px` has two values (vertical horizontal): `py-2 px-4`.
- `:hover` is the `hover:` prefix placed in front of the normal class.
- `transition: background-color 200ms` becomes `transition-colors duration-200`.

### 34.6 Worked Example: Absolutely Positioned Badge

```css
position: absolute;
top: -8px;
right: -8px;
z-index: 10;
```

```text
absolute -top-2 -right-2 z-10
```

- Negative values: put `-` in front of the utility: `-top-2`.
- Remember: the parent needs `relative`.

### 34.7 Worked Example: Responsive Grid

```css
display: grid;
grid-template-columns: 1fr;
gap: 24px;
@media (min-width: 768px)  { grid-template-columns: repeat(2, 1fr); }
@media (min-width: 1024px) { grid-template-columns: repeat(3, 1fr); }
```

```text
grid grid-cols-1 gap-6 md:grid-cols-2 lg:grid-cols-3
```

- `repeat(n, 1fr)` is `grid-cols-n`.
- `@media (min-width: ...)` is a breakpoint prefix; the un-prefixed class is the mobile default.

### 34.8 Quick Property-to-Prefix Dictionary

| CSS property | Tailwind prefix | Value style |
|---|---|---|
| `margin` | `m`, `mx`, `my`, `mt`, `mr`, `mb`, `ml` | number (x4px) / `auto` |
| `padding` | `p`, `px`, `py`, `pt`, `pr`, `pb`, `pl` | number |
| `width` / `height` | `w` / `h` (`size` for both) | number, fraction, `full`, `screen`, `auto`, `fit` |
| `min-width` / `max-width` | `min-w` / `max-w` | number, `md`, `7xl`, `full`, `prose` |
| `font-size` | `text` | `xs`...`9xl` |
| `font-weight` | `font` | `thin`...`black` |
| `font-family` | `font` | `sans`, `serif`, `mono` |
| `line-height` | `leading` | `none`...`loose`, number |
| `letter-spacing` | `tracking` | `tighter`...`widest` |
| `color` | `text` | color-shade |
| `background-color` | `bg` | color-shade |
| `border-width` | `border` | none, `0`, `2`, `4`, `8` |
| `border-color` | `border` | color-shade |
| `border-radius` | `rounded` | `sm`...`3xl`, `full` |
| `box-shadow` | `shadow` | `xs`...`2xl` |
| `opacity` | `opacity` | 0 to 100 |
| `display` | (the value itself) | `flex`, `grid`, `block`, `hidden` |
| `justify-content` | `justify` | `start`, `center`, `between`... |
| `align-items` | `items` | `start`, `center`, `end`... |
| `align-self` | `self` | |
| `flex-direction` | `flex` | `row`, `col` |
| `flex-wrap` | `flex` | `wrap`, `nowrap` |
| `gap` | `gap`, `gap-x`, `gap-y` | number |
| `grid-template-columns` | `grid-cols` | 1 to 12 |
| `position` | (the value itself) | `relative`, `absolute`... |
| `top/right/bottom/left` | `top`, `right`, `bottom`, `left`, `inset` | number, fraction |
| `z-index` | `z` | number |
| `overflow` | `overflow` | `hidden`, `auto`... |
| `cursor` | `cursor` | `pointer`... |
| `transition` | `transition`, `duration`, `ease`, `delay` | |
| `transform: scale/rotate/translate` | `scale`, `rotate`, `translate-x/y` | |
| `object-fit` | `object` | `cover`, `contain` |
| `aspect-ratio` | `aspect` | `square`, `video`, `[4/3]` |


---


## 35. Tailwind Cheat Tables

Compact lookup tables. Scan the left column for the category, the right for every class.

### 35.1 Typography

| Group | Classes |
|---|---|
| Family | `font-sans` `font-serif` `font-mono` |
| Size | `text-xs` `text-sm` `text-base` `text-lg` `text-xl` `text-2xl` `text-3xl` `text-4xl` `text-5xl` `text-6xl` `text-7xl` `text-8xl` `text-9xl` |
| Weight | `font-thin` `font-extralight` `font-light` `font-normal` `font-medium` `font-semibold` `font-bold` `font-extrabold` `font-black` |
| Style | `italic` `not-italic` `antialiased` |
| Align | `text-left` `text-center` `text-right` `text-justify` `text-start` `text-end` |
| Leading | `leading-none` `leading-tight` `leading-snug` `leading-normal` `leading-relaxed` `leading-loose` `leading-6` |
| Tracking | `tracking-tighter` `tracking-tight` `tracking-normal` `tracking-wide` `tracking-wider` `tracking-widest` |
| Decoration | `underline` `overline` `line-through` `no-underline` `decoration-wavy` `decoration-2` `underline-offset-4` |
| Transform | `uppercase` `lowercase` `capitalize` `normal-case` |
| Overflow | `truncate` `text-ellipsis` `text-clip` `line-clamp-1..6` |
| Whitespace | `whitespace-normal` `whitespace-nowrap` `whitespace-pre` `whitespace-pre-line` `whitespace-pre-wrap` `whitespace-break-spaces` |
| Breaking | `break-normal` `break-words` `break-all` `break-keep` `text-balance` `text-pretty` `text-wrap` `text-nowrap` |
| Numbers | `tabular-nums` `proportional-nums` `lining-nums` `oldstyle-nums` `slashed-zero` `ordinal` |

### 35.2 Spacing

| Group | Classes |
|---|---|
| Margin | `m-n` `mx-n` `my-n` `mt-n` `mr-n` `mb-n` `ml-n` `ms-n` `me-n` `m-auto` `mx-auto` `-m-n` `-mt-n` |
| Padding | `p-n` `px-n` `py-n` `pt-n` `pr-n` `pb-n` `pl-n` `ps-n` `pe-n` |
| Gap | `gap-n` `gap-x-n` `gap-y-n` |
| Space between | `space-x-n` `space-y-n` `space-x-reverse` `space-y-reverse` |
| Scale (n x 4px) | `0` `px` `0.5` `1` `1.5` `2` `2.5` `3` `3.5` `4` `5` `6` `7` `8` `9` `10` `11` `12` `14` `16` `20` `24` `28` `32` `36` `40` `44` `48` `52` `56` `60` `64` `72` `80` `96` |

### 35.3 Colors

| Group | Classes |
|---|---|
| Shades | `50` `100` `200` `300` `400` `500` `600` `700` `800` `900` `950` |
| Vivid hues | `red` `orange` `amber` `yellow` `lime` `green` `emerald` `teal` `cyan` `sky` `blue` `indigo` `violet` `purple` `fuchsia` `pink` `rose` |
| Neutral hues | `slate` `gray` `zinc` `neutral` `stone` (v4.2+: `mauve` `olive` `mist` `taupe`) |
| Special | `black` `white` `transparent` `current` `inherit` |
| Where colors apply | `text-` `bg-` `border-` `ring-` `ring-offset-` `inset-ring-` `divide-` `outline-` `shadow-` `inset-shadow-` `drop-shadow-` `decoration-` `accent-` `caret-` `fill-` `stroke-` `from-` `via-` `to-` `placeholder:text-` `selection:bg-` |
| Opacity | `bg-black/50` `text-white/80` `border-blue-500/30` `bg-blue-500/[0.35]` |
| Arbitrary | `bg-[#1e293b]` `text-[rgb(20,30,40)]` `bg-[oklch(0.7_0.15_200)]` `bg-(--brand)` |

### 35.4 Width

| Group | Classes |
|---|---|
| Fixed | `w-0` `w-px` `w-1` `w-4` `w-8` `w-10` `w-12` `w-16` `w-24` `w-32` `w-48` `w-64` `w-96` |
| Fractions | `w-1/2` `w-1/3` `w-2/3` `w-1/4` `w-3/4` `w-1/5` `w-1/6` `w-5/12` |
| Keywords | `w-full` `w-screen` `w-dvw` `w-auto` `w-fit` `w-min` `w-max` |
| Min | `min-w-0` `min-w-full` `min-w-min` `min-w-max` `min-w-fit` |
| Max | `max-w-xs` `max-w-sm` `max-w-md` `max-w-lg` `max-w-xl` `max-w-2xl` `max-w-3xl` `max-w-4xl` `max-w-5xl` `max-w-6xl` `max-w-7xl` `max-w-prose` `max-w-full` `max-w-screen` `max-w-none` |
| Both | `size-4` `size-10` `size-full` `size-px` `size-[72px]` |

### 35.5 Height

| Group | Classes |
|---|---|
| Fixed | `h-0` `h-px` `h-4` `h-8` `h-10` `h-12` `h-16` `h-24` `h-32` `h-48` `h-64` `h-96` |
| Keywords | `h-full` `h-screen` `h-dvh` `h-svh` `h-lvh` `h-auto` `h-fit` `h-min` `h-max` |
| Fractions | `h-1/2` `h-1/3` `h-2/3` `h-1/4` |
| Min | `min-h-0` `min-h-full` `min-h-screen` `min-h-dvh` `min-h-fit` |
| Max | `max-h-48` `max-h-96` `max-h-full` `max-h-screen` `max-h-none` |
| Arbitrary | `h-[500px]` `h-[calc(100dvh-4rem)]` |

### 35.6 Flex

| Group | Classes |
|---|---|
| Display | `flex` `inline-flex` |
| Direction | `flex-row` `flex-row-reverse` `flex-col` `flex-col-reverse` |
| Wrap | `flex-wrap` `flex-nowrap` `flex-wrap-reverse` |
| Justify (main axis) | `justify-start` `justify-center` `justify-end` `justify-between` `justify-around` `justify-evenly` |
| Items (cross axis) | `items-start` `items-center` `items-end` `items-baseline` `items-stretch` |
| Content (multi-line) | `content-start` `content-center` `content-end` `content-between` `content-around` `content-evenly` |
| Self | `self-auto` `self-start` `self-center` `self-end` `self-stretch` `self-baseline` |
| Item sizing | `flex-1` `flex-auto` `flex-initial` `flex-none` `grow` `grow-0` `shrink` `shrink-0` `basis-1/2` `basis-full` `basis-auto` |
| Order | `order-1` `order-2` `order-first` `order-last` `order-none` |

### 35.7 Grid

| Group | Classes |
|---|---|
| Display | `grid` `inline-grid` |
| Columns | `grid-cols-1` ... `grid-cols-12` `grid-cols-none` `grid-cols-subgrid` `grid-cols-[200px_1fr]` |
| Rows | `grid-rows-1` ... `grid-rows-12` `grid-rows-none` `grid-rows-[auto_1fr_auto]` |
| Column span/position | `col-span-1..12` `col-span-full` `col-start-1..13` `col-end-1..13` `col-auto` |
| Row span/position | `row-span-1..12` `row-span-full` `row-start-1..13` `row-end-1..13` `row-auto` |
| Flow | `grid-flow-row` `grid-flow-col` `grid-flow-dense` `grid-flow-row-dense` `grid-flow-col-dense` |
| Auto size | `auto-cols-auto` `auto-cols-min` `auto-cols-max` `auto-cols-fr` `auto-rows-auto` `auto-rows-min` `auto-rows-max` `auto-rows-fr` |
| Place | `place-items-center` `place-content-center` `place-self-center` `justify-items-*` `justify-self-*` |

### 35.8 Position

| Group | Classes |
|---|---|
| Type | `static` `relative` `absolute` `fixed` `sticky` |
| Inset | `inset-0` `inset-x-0` `inset-y-0` `top-0` `right-0` `bottom-0` `left-0` `start-0` `end-0` `inset-auto` |
| Offsets | `top-4` `-top-2` `top-1/2` `left-1/2` `top-full` `top-[10px]` |
| Z-index | `z-0` `z-10` `z-20` `z-30` `z-40` `z-50` `z-auto` `-z-10` `z-[100]` |
| Visibility | `visible` `invisible` `collapse` |
| Overflow | `overflow-auto` `overflow-hidden` `overflow-clip` `overflow-visible` `overflow-scroll` `overflow-x-auto` `overflow-y-auto` |

### 35.9 Border

| Group | Classes |
|---|---|
| Width | `border` `border-0` `border-2` `border-4` `border-8` |
| Sides | `border-x` `border-y` `border-t` `border-r` `border-b` `border-l` `border-s` `border-e` |
| Style | `border-solid` `border-dashed` `border-dotted` `border-double` `border-hidden` `border-none` |
| Color | `border-gray-200` `border-blue-500` `border-transparent` `border-current` `border-blue-500/30` |
| Divide | `divide-x` `divide-y` `divide-x-2` `divide-gray-200` `divide-dashed` |
| Ring | `ring` `ring-0` `ring-1` `ring-2` `ring-3` `ring-4` `ring-8` `ring-blue-500` `ring-offset-2` `inset-ring` |
| Outline | `outline` `outline-2` `outline-offset-2` `outline-dashed` `outline-hidden` `outline-none` |

### 35.10 Radius

| Group | Classes |
|---|---|
| Sizes | `rounded-none` `rounded-xs` `rounded-sm` `rounded-md` `rounded-lg` `rounded-xl` `rounded-2xl` `rounded-3xl` `rounded-4xl` `rounded-full` |
| Sides | `rounded-t-*` `rounded-r-*` `rounded-b-*` `rounded-l-*` `rounded-s-*` `rounded-e-*` |
| Corners | `rounded-tl-*` `rounded-tr-*` `rounded-br-*` `rounded-bl-*` `rounded-ss-*` `rounded-se-*` `rounded-es-*` `rounded-ee-*` |
| Pixels | 2px `xs`, 4px `sm`, 6px `md`, 8px `lg`, 12px `xl`, 16px `2xl`, 24px `3xl`, 32px `4xl` |

### 35.11 Shadow

| Group | Classes |
|---|---|
| Box shadow | `shadow-2xs` `shadow-xs` `shadow-sm` `shadow-md` `shadow-lg` `shadow-xl` `shadow-2xl` `shadow-none` |
| Colored | `shadow-blue-500/50` `shadow-black/10` |
| Inset | `inset-shadow-2xs` `inset-shadow-xs` `inset-shadow-sm` `inset-shadow-none` |
| Drop shadow (filter) | `drop-shadow-xs` `drop-shadow-sm` `drop-shadow-md` `drop-shadow-lg` `drop-shadow-xl` `drop-shadow-2xl` `drop-shadow-none` |
| Text shadow (v4.1+) | `text-shadow-2xs` `text-shadow-xs` `text-shadow-sm` `text-shadow-md` `text-shadow-lg` |
| Custom | `shadow-[0_4px_20px_rgba(0,0,0,0.15)]` |

### 35.12 Responsive

| Group | Classes |
|---|---|
| Min-width (mobile first) | `sm:` 640px, `md:` 768px, `lg:` 1024px, `xl:` 1280px, `2xl:` 1536px |
| Max-width | `max-sm:` `max-md:` `max-lg:` `max-xl:` `max-2xl:` |
| Range | `md:max-lg:` |
| Arbitrary | `min-[900px]:` `max-[600px]:` |
| Container queries | `@container` `@sm:` `@md:` `@lg:` `@xl:` `@max-md:` `@container/name` |
| Media features | `dark:` `print:` `motion-safe:` `motion-reduce:` `portrait:` `landscape:` `pointer-coarse:` `contrast-more:` |

### 35.13 States

| Group | Classes |
|---|---|
| Pointer and focus | `hover:` `focus:` `focus-visible:` `focus-within:` `active:` `visited:` `target:` |
| Form | `disabled:` `enabled:` `checked:` `indeterminate:` `default:` `required:` `optional:` `valid:` `invalid:` `user-valid:` `user-invalid:` `in-range:` `out-of-range:` `placeholder-shown:` `autofill:` `read-only:` |
| Structure | `first:` `last:` `only:` `odd:` `even:` `first-of-type:` `last-of-type:` `only-of-type:` `empty:` `nth-3:` `has-[...]:` `not-*:` `*:` `**:` |
| Pseudo-elements | `before:` `after:` `placeholder:` `file:` `marker:` `selection:` `first-letter:` `first-line:` `backdrop:` |
| Parent / sibling | `group-hover:` `group-focus:` `group-active:` `group-disabled:` `group-has-[...]:` `peer-checked:` `peer-focus:` `peer-invalid:` `peer-disabled:` `peer-hover:` |
| Attributes | `aria-expanded:` `aria-checked:` `aria-selected:` `aria-disabled:` `data-[state=open]:` `open:` |

### 35.14 Animation and Transition

| Group | Classes |
|---|---|
| Property | `transition` `transition-all` `transition-colors` `transition-opacity` `transition-shadow` `transition-transform` `transition-none` |
| Duration | `duration-75` `duration-100` `duration-150` `duration-200` `duration-300` `duration-500` `duration-700` `duration-1000` |
| Easing | `ease-linear` `ease-in` `ease-out` `ease-in-out` |
| Delay | `delay-75` `delay-100` `delay-150` `delay-200` `delay-300` `delay-500` `delay-700` `delay-1000` |
| Keyframe animations | `animate-spin` `animate-ping` `animate-pulse` `animate-bounce` `animate-none` |
| Accessibility | `motion-safe:` `motion-reduce:` |
| Entry | `starting:opacity-0` |

### 35.15 Transform

| Group | Classes |
|---|---|
| Scale | `scale-0` `scale-50` `scale-75` `scale-90` `scale-95` `scale-100` `scale-105` `scale-110` `scale-125` `scale-150` `scale-x-*` `scale-y-*` |
| Rotate | `rotate-0` `rotate-1` `rotate-2` `rotate-3` `rotate-6` `rotate-12` `rotate-45` `rotate-90` `rotate-180` `-rotate-*` |
| Translate | `translate-x-*` `translate-y-*` `-translate-x-*` `translate-x-1/2` `-translate-y-full` |
| Skew | `skew-x-*` `skew-y-*` `-skew-x-*` |
| Origin | `origin-center` `origin-top` `origin-top-right` `origin-right` `origin-bottom-right` `origin-bottom` `origin-bottom-left` `origin-left` `origin-top-left` |
| 3D | `transform-3d` `perspective-*` `rotate-x-*` `rotate-y-*` `backface-hidden` |

### 35.16 Effects and Filters

| Group | Classes |
|---|---|
| Opacity | `opacity-0` `opacity-25` `opacity-50` `opacity-75` `opacity-100` |
| Blur | `blur-xs` `blur-sm` `blur-md` `blur-lg` `blur-xl` `blur-2xl` `blur-3xl` |
| Brightness / contrast | `brightness-50` `brightness-75` `brightness-110` `brightness-125` `contrast-50` `contrast-125` `contrast-150` |
| Color filters | `grayscale` `sepia` `invert` `saturate-0` `saturate-150` `hue-rotate-90` |
| Backdrop | `backdrop-blur-sm` `backdrop-blur-md` `backdrop-blur-lg` `backdrop-brightness-50` `backdrop-saturate-150` `backdrop-contrast-125` |
| Blend | `mix-blend-multiply` `mix-blend-screen` `mix-blend-overlay` `bg-blend-multiply` |
| Misc | `isolate` `box-decoration-clone` `box-decoration-slice` |
| Objects | `object-cover` `object-contain` `object-fill` `object-none` `object-scale-down` `object-center` `object-top` |
| Aspect | `aspect-auto` `aspect-square` `aspect-video` `aspect-[4/3]` |


---

## 36. Common Mistakes

### 36.1 Using Invalid Class Names

Tailwind silently ignores classes it does not know: no error, no style.

| Wrong (invalid or outdated) | Right |
|---|---|
| `text-bold` | `font-bold` |
| `font-24` | `text-2xl` or `text-[24px]` |
| `margin-4`, `padding-4` | `m-4`, `p-4` |
| `center` | `text-center` or `flex justify-center` |
| `bg-color-blue` | `bg-blue-500` |
| `border-radius-lg` | `rounded-lg` |
| `flex-center` | `flex items-center justify-center` |
| `w-100` (in v3 not valid; in v4 means 25rem) | `w-full` (or `w-96`) |
| `rounded-md-2` | `rounded-md` |
| `text-color-red` | `text-red-500` |
| `bg-opacity-50` (removed in v4) | `bg-black/50` |
| `flex-shrink-0` (removed in v4) | `shrink-0` |
| `shadow-inner` (v3) | `inset-shadow-sm` |

**How to catch them:** install **Tailwind CSS IntelliSense**; unknown classes get a squiggle, and hovering any valid class shows its CSS.

### 36.2 Forgetting Mobile-First Behavior

```html
<!-- WRONG: expecting "sm:" to mean phones. This is hidden on phones too. -->
<div class="sm:hidden">...</div>   <!-- hidden from 640px UP, visible below -->

<!-- Think it through: un-prefixed = all sizes; prefixed = from that size upward -->
<div class="block md:hidden">Mobile only</div>
<div class="hidden md:block">Desktop only</div>
```

Design the **mobile layout first** with plain classes, then add `md:` and `lg:` for larger screens. Do not start with `lg:` classes and try to patch mobile afterwards.

### 36.3 Confusing justify-* and items-*

- `justify-*` = **main axis** (horizontal in `flex-row`).
- `items-*` = **cross axis** (vertical in `flex-row`).
- After `flex-col`, they swap visual directions.

```html
<div class="flex justify-center items-center">...</div>   <!-- center both ways -->
<div class="flex flex-col items-center">...</div>          <!-- column, centered horizontally -->
```

If something does not center vertically, the parent usually has no height: add `h-screen`, `min-h-screen`, or `h-64`.

### 36.4 Overusing Arbitrary Values

```html
<!-- Over-specified: ignores the design scale -->
<div class="mt-[16px] p-[24px] text-[#3b82f6] rounded-[8px] w-[100%]">

<!-- Same result with the scale -->
<div class="mt-4 p-6 text-blue-500 rounded-lg w-full">
```

Prefer scale values. If you keep using one custom value, add it to `@theme`.

### 36.5 Incorrect Responsive Classes

| Mistake | Fix |
|---|---|
| `md:text-lg text-sm` works but is confusing | write base first: `text-sm md:text-lg` |
| Using `sm:` to target phones | un-prefixed is the phone style |
| `md:hidden lg:block` when you wanted only desktop | `hidden lg:block` |
| Unsorted breakpoints in thinking (`lg:` then `md:`) | order mentally `sm`, `md`, `lg`, `xl`, `2xl` |
| Expecting `container` to center | add `mx-auto px-4` |

### 36.6 Tailwind v3 vs v4 Confusion

| Symptom | Cause | Fix |
|---|---|---|
| `bg-opacity-*` does nothing | removed in v4 | `bg-black/50` |
| Borders look black or dark | default color is now `currentColor` | always add `border-gray-200` |
| `ring` looks thin | v4 `ring` = 1px | use `ring-3` |
| Shadows or radii look smaller | scale renamed one step | v3 `shadow` becomes `shadow-sm`; v3 `rounded` becomes `rounded-sm` |
| `@tailwind base;` has no effect | v3 directive | `@import "tailwindcss";` |
| `tailwind.config.js` is ignored | v4 is CSS-first | use `@theme` in CSS, or `@config` |
| `dark:` ignores your `.dark` class | v4 default is media-based | add `@custom-variant dark (&:where(.dark, .dark *));` |
| `outline-none` removes accessibility | semantics changed | use `outline-hidden` |
| Buttons no longer show a pointer | v4 preflight change | add `cursor-pointer` |
| `bg-[--brand]` fails | old variable syntax | `bg-(--brand)` |
| `hover:` does nothing on a phone | v4 only applies on hover-capable devices | design for tap with `active:` |

**Which version am I on?** Check `package.json` (`"tailwindcss": "^4..."`) and your CSS entry (`@import "tailwindcss"` means v4).

### 36.7 Dynamic Class Names Tailwind Cannot Detect

Tailwind finds classes by scanning your source files **as plain text**. It does not run your JavaScript. A class name assembled from pieces never appears as a complete string, so its CSS is never generated.

```jsx
// WRONG: Tailwind never sees "bg-red-500" or "bg-blue-500"
<div className={`bg-${color}-500`} />
<div className={'text-' + size} />

// RIGHT: complete class names, chosen by logic
const colors = {
  red:  'bg-red-500',
  blue: 'bg-blue-500',
}
<div className={colors[color]} />

// RIGHT: ternary with full strings
<div className={isError ? 'text-red-600' : 'text-green-600'} />
```

For truly dynamic numbers (user-chosen pixel values, API colors) use the **style prop** or a CSS variable:

```jsx
<div style={{ width: `${percent}%`, backgroundColor: userColor }} />
<div className="w-(--w)" style={{ '--w': `${percent}%` }} />
```

### 36.8 Missing Source Detection / Configuration

- **v4:** classes are detected automatically from your project (respecting `.gitignore`). If styles are missing from a **library in `node_modules`**, another folder, or a file type Tailwind skips, add `@source "../node_modules/some-ui-lib";` in your CSS.
- **v3:** the `content` array in `tailwind.config.js` must list every file with classes (`"./src/**/*.{js,jsx,ts,tsx}"`). A missing path means missing styles in production.
- Make sure your CSS file (with `@import "tailwindcss"`) is actually imported in `main.jsx` and the Vite plugin is registered.
- Restart the dev server after changing config.

### 36.9 Using @apply Unnecessarily

```css
/* Avoid: you are just rebuilding old-style CSS and losing Tailwind's benefits */
.btn { @apply px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700; }
```

In React, **make a component** instead:

```jsx
function Button({ children }) {
  return <button className="rounded-lg bg-blue-600 px-4 py-2 text-white hover:bg-blue-700">{children}</button>
}
```

`@apply` is fine for styling markup you cannot control (CMS content, third-party widgets) or tiny base styles. In Vue, Svelte or CSS Modules you may need `@reference "../app.css";` at the top of the stylesheet to use `@apply`.

### 36.10 Specificity and Override Problems

- Tailwind utilities are **flat** (single class). Order in the `class` attribute does **not** decide who wins; the order of rules in the generated stylesheet does.
- `class="p-4 p-8"` is unpredictable. Never put conflicting utilities on the same element. In React components that accept `className`, merge with **`tailwind-merge`** ([Section 37](#37-react--tailwind-notes)).
- A plain CSS rule can beat utilities or lose to them depending on layers. In v4, Tailwind uses CSS `@layer`; unlayered custom CSS **beats** utilities. Put custom component CSS inside `@layer components { ... }` or use utilities.
- Third-party CSS that wins: add your own `!` modifier as a last resort (`text-red-500!`).

### 36.11 Important Modifier Misuse

```html
<!-- Bad: using ! to cover up your own conflicting classes -->
<p class="text-gray-500 text-red-500!">

<!-- Better: just remove the conflict -->
<p class="text-red-500">
```

Using `!` widely makes every later override require another `!`. Reserve it for third-party CSS and rare inline-style fights.

### 36.12 Other Frequent Mistakes

| Mistake | Fix |
|---|---|
| `h-full` does nothing | parent needs a height (`h-screen`, `min-h-screen`, or flex/grid sizing) |
| Flex child will not truncate | add `min-w-0` to the flex child |
| `absolute` element flies to the page corner | add `relative` to the parent |
| `sticky` does nothing | add `top-0`; remove `overflow-hidden` from ancestors |
| `z-10` has no effect | element needs a position (`relative`, `absolute`, `fixed`, `sticky`) or be a flex/grid item |
| `w-screen` causes horizontal scroll | use `w-full` (the scrollbar width is included in 100vw) |
| Text color not changing | check you used `text-` for color and not just size |
| List bullets missing | Tailwind resets lists: add `list-disc pl-5` |
| Image stretched | add `object-cover` (or `object-contain`) with a set width and height |
| Hover effect jumps | add `transition` and consider `transform` instead of changing layout size |
| Heading sizes all look the same | the reset removes default `h1`-`h6` sizes: set `text-*` and `font-*` yourself |
| Forgot `<meta name="viewport" ...>` | responsive classes will not work on phones without it |
| Gradient shows no color | needs `bg-linear-to-*` **and** a `from-` color |

---

## 37. React + Tailwind Notes

### 37.1 className, Not class

```jsx
// HTML:  <div class="p-4 bg-blue-500 text-white rounded-lg">
<div className="p-4 bg-blue-500 text-white rounded-lg">Hello</div>
```

Other JSX differences: `for` becomes `htmlFor`; self-close `<input />` and `<img />`; inline styles take objects (`style={{ width: 20 }}`).

### 37.2 Conditional Classes: Ternary

```jsx
function Button({ primary }) {
  return (
    <button className={primary ? 'bg-blue-600 text-white' : 'bg-gray-100 text-gray-900'}>
      Click
    </button>
  )
}
```

### 37.3 Template Literals (for combining static + conditional)

```jsx
<button className={`rounded-lg px-4 py-2 ${active ? 'bg-blue-600 text-white' : 'bg-gray-100'}`}>
  Tab
</button>
```

**Pitfalls:** an empty condition can leave stray spaces (harmless); and **never build the class name from parts** (`bg-${color}-500`): see [Section 36.7](#367-dynamic-class-names-tailwind-cannot-detect). Template literals get unreadable with many conditions: use `clsx`.

### 37.4 clsx (clean conditional classes)

```bash
npm install clsx
```

```jsx
import clsx from 'clsx'

<button
  className={clsx(
    'rounded-lg px-4 py-2 font-medium transition',      // always
    active && 'bg-blue-600 text-white',                  // if true
    !active && 'bg-gray-100 text-gray-900',              // if false
    disabled && 'cursor-not-allowed opacity-50',
    { 'ring-2 ring-blue-500': focused }                  // object form
  )}
/>
```

`clsx` ignores `false`, `null` and `undefined`, so `condition && 'class'` is safe.

### 37.5 tailwind-merge and the cn() Helper

Problem: a reusable component with `p-4` receives `className="p-8"`. Both classes are present and the winner is unpredictable. `tailwind-merge` resolves conflicts so the **last** one wins.

```bash
npm install clsx tailwind-merge
```

```js
// src/lib/cn.js
import { clsx } from 'clsx'
import { twMerge } from 'tailwind-merge'

export function cn(...inputs) {
  return twMerge(clsx(inputs))
}
```

```jsx
import { cn } from '../lib/cn'

function Card({ className, children }) {
  return <div className={cn('rounded-xl bg-white p-4 shadow', className)}>{children}</div>
}

<Card className="p-8 bg-gray-50">...</Card>   // result: rounded-xl shadow p-8 bg-gray-50
```

Make sure you use a `tailwind-merge` version that supports Tailwind v4 (v3.x of the package).

### 37.6 Variant Maps (safe dynamic styling)

Use an object whose values are **complete class strings**:

```jsx
const variants = {
  primary:   'bg-blue-600 text-white hover:bg-blue-700',
  secondary: 'bg-gray-100 text-gray-900 hover:bg-gray-200',
  danger:    'bg-red-600 text-white hover:bg-red-700',
}
const sizes = {
  sm: 'px-3 py-1.5 text-sm',
  md: 'px-4 py-2 text-base',
  lg: 'px-6 py-3 text-lg',
}

export function Button({ variant = 'primary', size = 'md', className, ...props }) {
  return (
    <button
      className={cn(
        'inline-flex items-center justify-center rounded-lg font-medium transition',
        'focus-visible:ring-2 focus-visible:ring-blue-500 focus-visible:ring-offset-2',
        'disabled:cursor-not-allowed disabled:opacity-50',
        variants[variant],
        sizes[size],
        className
      )}
      {...props}
    />
  )
}

// <Button variant="danger" size="lg">Delete</Button>
```

For large design systems, the **`class-variance-authority` (cva)** library formalizes exactly this pattern.

### 37.7 Reusable Component Styling

- **Extract components, not CSS classes.** Repeat markup? Make a `<Card>`, `<Badge>`, `<Button>`.
- Accept a `className` prop and merge it with `cn()` so callers can tweak.
- Spread remaining props (`{...props}`) so `onClick`, `type`, `aria-*` pass through.
- Keep one place for each variant map.

```jsx
export function Badge({ tone = 'gray', children }) {
  const tones = {
    gray:  'bg-gray-100 text-gray-700',
    green: 'bg-green-100 text-green-800',
    red:   'bg-red-100 text-red-800',
  }
  return <span className={cn('inline-flex rounded-full px-2.5 py-0.5 text-xs font-medium', tones[tone])}>{children}</span>
}
```

### 37.8 Styling by State with Data Attributes

Let React set a `data-*` attribute and style it with Tailwind variants. No string juggling.

```jsx
<button
  data-active={isActive}
  className="rounded-lg px-4 py-2 data-[active=true]:bg-blue-600 data-[active=true]:text-white"
>
  Tab
</button>

<div aria-expanded={open} className="group">
  <svg className="size-4 transition-transform group-aria-expanded:rotate-180" />
</div>
```

### 37.9 Truly Dynamic Values

```jsx
// Progress bar width from state: use style (or a CSS variable)
<div className="h-2 rounded-full bg-gray-200">
  <div className="h-2 rounded-full bg-blue-600 transition-all" style={{ width: `${progress}%` }} />
</div>

// CSS variable pattern: keep Tailwind classes, feed in the number
<div className="size-(--size) rounded-full bg-blue-500" style={{ '--size': `${px}px` }} />
```

### 37.10 Lists, Mapping and Layout in React

```jsx
export default function ProductGrid({ products }) {
  return (
    <div className="grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
      {products.map(p => (
        <article key={p.id} className="group overflow-hidden rounded-xl border border-gray-200 bg-white">
          <img className="aspect-square w-full object-cover transition duration-300 group-hover:scale-105" src={p.image} alt={p.name} />
          <div className="p-4">
            <h3 className="font-semibold text-gray-900">{p.name}</h3>
            <p className="text-gray-500">${p.price}</p>
          </div>
        </article>
      ))}
    </div>
  )
}
```

### 37.11 Handy React + Tailwind Checklist

- Use `className`. Never concatenate partial class names. Keep full strings.
- Use `clsx`/`cn` once you have more than one condition.
- Use `tailwind-merge` in components that accept `className`.
- Use data/aria attributes for state styling.
- Use `style` or CSS variables for runtime numbers and colors.
- Install **Tailwind CSS IntelliSense** and **prettier-plugin-tailwindcss** (add `tailwindFunctions: ["clsx", "cn"]` to Prettier config to sort classes inside those calls).
- Keep class lists readable: break long lists across lines inside template strings or `cn()` calls, grouped by purpose (layout, spacing, color, state).

---

## Appendix: Mental Checklist When Styling Anything

1. **Layout:** `flex` / `grid` / `block`? Direction, alignment, gap.
2. **Size:** `w-` / `h-` / `max-w-` / `aspect-`.
3. **Spacing:** `p-` inside, `m-` outside (or `gap-`).
4. **Typography:** `text-` size, `font-` weight, `leading-`, color.
5. **Colors:** `bg-`, `text-`, `border-` with a shade (50-950).
6. **Shape:** `border`, `rounded-`, `shadow-`, `ring-`.
7. **States:** `hover:`, `focus-visible:`, `disabled:`, `dark:`.
8. **Responsive:** add `md:` / `lg:` overrides **after** the mobile layout works.
9. **Motion:** `transition`, `duration-`, `hover:scale-`.
10. **Accessibility:** focus ring, labels, `sr-only`, contrast.

*End of the Tailwind CSS Master Cheat Sheet (documenting Tailwind CSS v4.3).*
