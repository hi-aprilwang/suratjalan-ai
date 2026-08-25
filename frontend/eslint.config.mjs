import { defineConfig, globalIgnores } from "eslint/config";
import nextVitals from "eslint-config-next/core-web-vitals";
import nextTs from "eslint-config-next/typescript";

const eslintConfig = defineConfig([
  ...nextVitals,
  ...nextTs,
  {
    rules: {
      "no-restricted-syntax": [
        "error",
        {
          selector: "Literal[value=/(^|\\s)(text-xs|text-xxs|text-\\[\\s*([0-9]|1[0-2])px\\s*\\])($|\\s)/]",
          message: "XS-level typography (text-xs, text-[...px] <= 12px) is banned. Use text-sm or larger for accessibility and readability."
        },
        {
          selector: "TemplateElement[value.raw=/(^|\\s)(text-xs|text-xxs|text-\\[\\s*([0-9]|1[0-2])px\\s*\\])($|\\s)/]",
          message: "XS-level typography (text-xs, text-[...px] <= 12px) is banned. Use text-sm or larger for accessibility and readability."
        }
      ]
    }
  },
  // Override default ignores of eslint-config-next.
  globalIgnores([
    // Default ignores of eslint-config-next:
    ".next/**",
    "out/**",
    "build/**",
    "next-env.d.ts",
  ]),
]);

export default eslintConfig;
