import * as validators from '@vuelidate/validators';
import { createI18nMessage } from '@vuelidate/validators';
import { createI18n } from 'vue-i18n';
import ru from '@/translate/ru.json';

const i18n = createI18n({
  locale: 'ru',
  allowComposition: true,
  messages: { ru },
});

const withI18nMessage = createI18nMessage({ t: i18n.global.t.bind(i18n) });

export const required = withI18nMessage(validators.required);
export const email = withI18nMessage(validators.email);
export const minLength = withI18nMessage(validators.minLength, { withArguments: true });
export const sameAs = withI18nMessage(validators.sameAs, { withArguments: true });
export const url = withI18nMessage(validators.url);
export const minValue = withI18nMessage(validators.minValue, { withArguments: true });
export const maxValue = withI18nMessage(validators.maxValue, { withArguments: true });
